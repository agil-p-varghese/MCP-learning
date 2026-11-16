from mcp.server.fastmcp import FastMCP

# Initialize FastMCP directly from the official SDK
mcp = FastMCP("calculator_mcp")

@mcp.tool()
def add(a: float, b: float) -> float:
    """Add two numbers together"""
    return a + b

@mcp.tool()
def multiply(a: float, b: float) -> float:
    """Multiply two numbers together"""
    return a * b

if __name__ == "__main__":
    # Runs using the standard transport
    mcp.run(transport="http",host="localhost",port=8002)#http