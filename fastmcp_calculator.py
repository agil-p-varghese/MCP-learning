#libraries
from fastmcp import FastMCP

mcp=FastMCP("Calculator")

@mcp.tool()
def multiply(a:float,b:float)->float:
    """Multiply two numbers.
    args:a(float) :the first number.
        b(float)  :the second number.

    returns:float :the product of two numbers.
    """
    return a*b

#second type of passing info
@mcp.tool(
    name="add",
    description="add two numbers",
    tags={"math","arithmatic"}
)
def add_numbers(a:float,b:float)->float:
    """Add two numbers.
    args:a(float) :the first number.
         b(float) :the second number.

    returns: the sum of two numbers."""
    return a+b

@mcp.tool()
def subtract(a:float,b:float)->float:
    """Subtract two numbers.
    args:a(float) the first number.
         b(float) the second number.
    
    returns:(float) the difference of two numbers."""
    return a-b

@mcp.tool()
def divide(a:float,b:float)->float:
    """divide two numbers.
    args:a(float) the first number.
         b(float) the second number.
    
    return:(float) :the quiotient of two numbers"""
    if b==0:
        raise ValueError("cannot divide by zero")
    return a/b

if __name__=="__main__":
    mcp.run()##STDIO by default
