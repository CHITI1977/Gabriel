from flask import Flask, jsonify
app = Flask(__name__)
@app.route("/")
def home():
return "AuroraStay Backend Running"
@app.route("/v1/relevant_chunks")
def relevant_chunks():
return jsonify({
"chunks": [
"Sample chunk 1",
"Sample chunk 2"
]
})
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)
