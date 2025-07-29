from mcp.server.fastmcp import FastMCP
from . import tool

mcp = FastMCP("host info mcp")
mcp.add_tool(tool.get_host_info)
    
def main():
    mcp.run("stdio") # sse

if __name__ == "__main__":
    main()