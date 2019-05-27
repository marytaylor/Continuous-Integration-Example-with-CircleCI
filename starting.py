from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
  return f"This is my library version: {__version__}"

if __name__ == "__main__":
  app.run()
