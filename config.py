"""
Discord bot configuration using environment variables and .env file support.

This module loads configuration from environment variables with .env file taking precedence.
The .env file values override system environment variables to ensure consistent configuration.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
# Use override=True to prioritize .env file over system environment variables
load_dotenv(override=True)

# Discord Bot Token (required)
# Environment variable: DISCORD_BOT_TOKEN
token = os.getenv('DISCORD_BOT_TOKEN')
if not token:
    raise ValueError("DISCORD_BOT_TOKEN environment variable is required")

# Pollinations API Key (required for LLM features)
# Environment variable: POLLINATIONS_API_KEY
# Get your token from https://auth.pollinations.ai
pollinations_api_key = os.getenv('POLLINATIONS_API_KEY')
if not pollinations_api_key:
    raise ValueError("POLLINATIONS_API_KEY environment variable is required")

# Legacy alias for backward compatibility
perplexity = pollinations_api_key

# LLM Model Configuration (optional)
# Environment variable: LLM_MODEL
# Default model is "gemini-search" for Pollinations (has web search capability)
# Other options: "openai", "mistral", "searchgpt"
llm_model = os.getenv('LLM_MODEL', 'gemini-search')

# Rate Limiting Configuration (optional)
# Environment variables: RATE_LIMIT_SECONDS, MAX_REQUESTS_PER_MINUTE
# Default values: 10 seconds cooldown, 6 requests per minute
rate_limit_seconds = int(os.getenv('RATE_LIMIT_SECONDS', '10'))
max_requests_per_minute = int(os.getenv('MAX_REQUESTS_PER_MINUTE', '6'))

# Firecrawl API Key (required for link scraping)
# Environment variable: FIRECRAWL_API_KEY
firecrawl_api_key = os.getenv('FIRECRAWL_API_KEY')
if not firecrawl_api_key:
    raise ValueError("FIRECRAWL_API_KEY environment variable is required")

# Firecrawl Timeout Configuration (optional)
# Environment variable: FIRECRAWL_TIMEOUT_MS
# Maximum duration in milliseconds before aborting a scrape request
# Default: 900000ms (15 minutes) - maximum practical value
firecrawl_timeout_ms = int(os.getenv('FIRECRAWL_TIMEOUT_MS', '900000'))

# Apify API Token (optional, for x.com/twitter.com link scraping)
# Environment variable: APIFY_API_TOKEN
# If not provided, Twitter/X.com links will be processed using Firecrawl
apify_api_token = os.getenv('APIFY_API_TOKEN')


# Daily Summary Configuration (optional)
# Environment variables: SUMMARY_HOUR, SUMMARY_MINUTE, REPORTS_CHANNEL_ID, SUMMARY_CHANNEL_IDS
# Default time: 00:00 UTC
summary_hour = int(os.getenv('SUMMARY_HOUR', '0'))
summary_minute = int(os.getenv('SUMMARY_MINUTE', '0'))
reports_channel_id = os.getenv('REPORTS_CHANNEL_ID')

# Optional: restrict daily summaries to specific channel IDs (comma-separated list of IDs)
_summary_channel_ids_raw = os.getenv('SUMMARY_CHANNEL_IDS')
if _summary_channel_ids_raw:
    summary_channel_ids = [cid.strip() for cid in _summary_channel_ids_raw.split(',') if cid.strip()]
else:
    summary_channel_ids = None

# Links Dump Channel Configuration (optional)
# Environment variable: LINKS_DUMP_CHANNEL_ID
# Channel where only links are allowed - text messages will be auto-deleted
links_dump_channel_id = os.getenv('LINKS_DUMP_CHANNEL_ID')

# LLM API Configuration (optional)
# Environment variable: LLM_BASE_URL
# Base URL for Pollinations API (OpenAI-compatible endpoint)
llm_base_url = os.getenv('LLM_BASE_URL', 'https://text.pollinations.ai/openai')

# Legacy alias for backward compatibility
perplexity_base_url = llm_base_url

# HTTP Headers Configuration (optional)
# Environment variables: HTTP_REFERER, X_TITLE
# Used in LLM API requests for tracking/identification
http_referer = os.getenv('HTTP_REFERER', 'https://techfren.net')
x_title = os.getenv('X_TITLE', 'TechFren Discord Bot')

# Summary Command Limits
# Maximum hours that can be requested in summary commands (7 days)
MAX_SUMMARY_HOURS = 168
# Performance threshold for large summaries (24 hours)
LARGE_SUMMARY_THRESHOLD = 24

# Error Messages
ERROR_MESSAGES = {
    'invalid_hours_range': f"Number of hours must be between 1 and {MAX_SUMMARY_HOURS} (7 days).",
    'invalid_hours_format': "Please provide a valid number of hours. Usage: `/sum-hr <number>` (e.g., `/sum-hr 10`)",
    'processing_error': "Sorry, an error occurred while processing your request. Please try again later.",
    'summary_error': "Sorry, an error occurred while generating the summary. Please try again later.",
    'large_summary_warning': "⚠️ Large summary requested ({hours} hours). This may take longer to process.",
    'no_query': "Please provide a query after mentioning the bot.",
    'rate_limit_cooldown': "Please wait {wait_time:.1f} seconds before making another request.",
    'rate_limit_exceeded': "You've reached the maximum number of requests per minute. Please try again in {wait_time:.1f} seconds.",
    'database_unavailable': "Sorry, a critical error occurred (database unavailable). Please try again later.",
    'database_error': "Sorry, a database connection error occurred. Please try again later.",
    'no_messages_found': "No messages found in this channel for the past {hours} hours."
}
