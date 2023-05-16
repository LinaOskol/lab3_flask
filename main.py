from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/', methods=['post', 'get'])
def form():
    if request.method == 'POST':
        summ = int(request.form.get('summ'))
        first_installment = int(request.form.get('first_installment'))
        credit = summ - first_installment
        month = int(request.form.get('month')) * 12
        percent = float(request.form.get('percent'))
        radios = request.form.get('gridRadios')
        if radios == 'option1':
            bet = percent / 12 / 100
            all_bet = (1 + bet) ** month
            # every_month=(credit*bet*all_bet)/(all_bet-1)
            return render_template('index.html', every_month=round((credit * bet * all_bet) / (all_bet - 1)),
                                   credite=round(summ - first_installment))
        elif radios == 'option2':
            debt = credit / month
            bet = percent / 12 / 100
            percent_part = credit * bet
            return render_template('index.html', every_month=round(debt + percent_part),
                                   credite=round(summ - first_installment))


if __name__ == '__main__':
    app.run()
