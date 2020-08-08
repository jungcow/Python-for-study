from flask import Flask, render_template, request

app = Flask('SuperScrapper')

@app.route('/')
def home():
  return render_template('potato.html')

@app.route('/report')
def report():
  word = request.args.get('word')
  return render_template('report.html', searchingBy = word)

print('hello')
app.run(host='0.0.0.0')

  <!-- <section>
    {& for content in contents %}
      <span>{{content.title}}</span>
    {% endfor %}
  </section> -->