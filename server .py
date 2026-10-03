from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "KAKU BOT SERVER ONLINE"

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json

    pair = data.get("pair", "EURUSD")
    timeframe = data.get("timeframe", "M1")

    # Abhi demo response.
    # Real MT5 analysis next step mein add karenge.
    signal = "WAIT"

    return jsonify({
        "signal": signal,
        "message": "KAKU server connected",
        "pair": pair,
        "timeframe": timeframe
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
