# pydantic_googleaddon/web_search.py

import asyncio
from typing import List, Dict, Any

class WebSearch:
    def __init__(self, agent, web_tool):
        self.agent = agent
        self.web_tool = web_tool
        # Register the search and browse capabilities
        agent.register_tool(self.search, "search", "Search the web for information")
        agent.register_tool(self.browse, "browse", "Get content from a specific URL")

    async def search(self) -> List[Dict[str, Any]]:
        """Search the web and return results."""
        query = await asyncio.get_event_loop().run_in_executor(None, input, "Enter your search query: ")
        if not query.strip():
            return []
            
        return self.web_tool.search(query)

    async def browse(self, url: str) -> str:
        """Get content from a specific URL."""
        if not self.web_tool.is_url(url):
            return f"Invalid URL: {url}"
        
        content = self.web_tool.get_web_content(url)
        if not content:
            return f"Could not retrieve content from {url}"
        
        return content
