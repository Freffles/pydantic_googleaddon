import asyncio
from web_tool import WebTool
from web_search import WebSearch

class MockAgent:
    def register_tool(self, func, name, description):
        pass  # Simple mock implementation

async def main():
    # Initialize the web tool with debug mode
    web_tool = WebTool(num_results=5)
    WebTool.DEBUG = True  # Enable debug logging
    
    # Create a mock agent and initialize WebSearch
    agent = MockAgent()
    web_search = WebSearch(agent, web_tool)
    
    try:
        print("\nInteractive Web Search")
        print("=" * 50)
        
        # Get search results
        results = await web_search.search()
        
        if not results:
            print("No results found or empty query provided.")
            return
            
        # Display results
        print("\nSearch Results:")
        print("=" * 50)
        for i, result in enumerate(results, 1):
            print(f"\n{i}. {result['title']}")
            print(f"   URL: {result['url']}")
            print(f"   Description: {result['description']}")
        
        # Get content from first result
        if results:
            first_url = results[0]['url']
            print(f"\nFetching content from first result: {first_url}")
            print("=" * 50)
            
            content = await web_search.browse(first_url)
            print("\nContent Preview:")
            print(content[:500] + "..." if len(content) > 500 else content)
            
    except Exception as e:
        print(f"Error occurred: {type(e).__name__}: {str(e)}")

if __name__ == "__main__":
    asyncio.run(main())
