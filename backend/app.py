from flask import Flask, jsonify
2
 
3
app = Flask(__name__)
4
 
5
@app.route("/")
6
def home():
7
return "AuroraStay Backend Running"
8
 
9
@app.route("/v1/relevant_chunks")
10
def relevant_chunks():
11
return jsonify({
12
"chunks": [
13
"Sample chunk 1",
14
"Sample chunk 2"
15
]
16
})
17
 
18
if __name__ == "__main__":
19
app.run(host="0.0.0.0", port=7860)
