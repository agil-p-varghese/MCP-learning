#HTTP
from fastapi import FastAPI

#1 lets make a fastapi app(that means api)
app=FastAPI(title="Calculator-api")

@app.post("/multiply")
def multiply_numbers(a:float,b:float)->float:
    """
    Multiply two numbers and returns the result.
    """
    result=a*b
    return result

@app.post("/divide")
def divide_numbers(a:float,b:float)->float:
    """
    divide two numbers and returns the result.
    """
    result=a/b
    return {"result":result}

@app.post("/add")
def add_numbers(a:float,b:float)->float:
    """
    Add two numbers and returns the result.
    """
    result=a+b
    return {"result":result}

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app,host="localhost",port=8000)