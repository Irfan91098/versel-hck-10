from fastapi import FastAPI, HTTPException, Header

app = FastAPI()

key = "hacktiv8mania2023"

# public
@app.get("/") # menentukan alamat/url
def helloFunction(): # function yang memproses alamat/url tertentu
    return {
        "message": "hello world"
    }

# secret -> harus memasukan authentication
@app.get("/secret")
def helloFunction(api_keys: str = Header(none)):
    # check api_key dari header
    if api_keys is none or api_keys != key:
        raise HTTPException(status_code=401, detail="Invalid API key")
    
    return {
        "message": "secret message"
    }
