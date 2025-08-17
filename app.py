from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# የጌሙን ነጥብ ከፋይል የሚያነሳ function
def load_score():
    try:
        with open("score.txt", "r") as f:
            return int(f.read())
    except FileNotFoundError:
        return 0 # ፋይሉ ከሌለ 0 ይጀምራል

# የጌሙን ነጥብ ወደ ፋይል የሚያስቀምጥ function
def save_score(score):
    with open("score.txt", "w") as f:
        f.write(str(score))

@app.route('/')
def index():
    current_score = load_score()
    return render_template('index.html', score=current_score)

@app.route('/click', methods=['POST'])
def click():
    current_score = load_score()
    current_score += 1 # አንድ ነጥብ ይጨምራል
    save_score(current_score)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
