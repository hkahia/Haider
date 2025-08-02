from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        query = request.form["search"]
        df = pd.read_excel("data.xlsx")
        match = df[df['الاسم'].astype(str).str.contains(query, na=False)][['الاسم', 'القسم']]
        result = match.to_html(index=False, classes="result-table") if not match.empty else "لا توجد نتائج"
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
