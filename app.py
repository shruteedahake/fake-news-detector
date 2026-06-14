from flask import Flask, render_template, request

app = Flask(__name__)

# Sample Dataset (10 records)
news_dataset = [
    {
        "statement": "India's Chandrayaan-3 successfully landed near the Moon's south pole on August 23, 2023",
        "label": "True"
    },
    {
        "statement": "India became the first country to land a spacecraft near the Moon's south polar region",
        "label": "True"
    },
    {
        "statement": "The World Health Organization declared COVID-19 a pandemic in March 2020",
        "label": "True"
    },
    {
        "statement": "The James Webb Space Telescope released its first full-color scientific images in 2022",
        "label": "True"
    },
    {
        "statement": "Scientists confirmed that climate change is contributing to more frequent extreme weather events",
        "label": "True"
    },
    {
        "statement": "The Paris Agreement is an international treaty focused on combating climate change",
        "label": "True"
    },
    {
        "statement": "Electric vehicles produce zero tailpipe emissions during operation",
        "label": "True"
    },
    {
        "statement": "The Pacific Ocean is the largest ocean on Earth",
        "label": "True"
    },
    {
        "statement": "India hosted the G20 Leaders Summit in New Delhi in 2023",
        "label": "True"
    },
    {
        "statement": "NASA's Perseverance rover is exploring Mars",
        "label": "True"
    },
    {
        "statement": "COVID-19 vaccines contain microchips used to track people",
        "label": "Fake"
    },
    {
        "statement": "5G mobile towers spread coronavirus through radio waves",
        "label": "Fake"
    },
    {
        "statement": "NASA confirmed that Earth will experience six days of darkness next month",
        "label": "Fake"
    },
    {
        "statement": "Drinking bleach can cure viral infections",
        "label": "Fake"
    },
    {
        "statement": "The Moon is made entirely of cheese",
        "label": "Fake"
    },
    {
        "statement": "Humans only use 10 percent of their brains",
        "label": "Fake"
    },
    {
        "statement": "Vaccines cause autism in children",
        "label": "Fake"
    },
    {
        "statement": "A viral message claims currency notes contain secret tracking chips",
        "label": "Fake"
    },
    {
        "statement": "The Earth is flat and governments are hiding the truth",
        "label": "Fake"
    },
    {
        "statement": "Sharks are attracted to WiFi signals emitted by smartphones",
        "label": "Fake"
    }
]


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/detect', methods=['POST'])
def detect():
    user_statement = request.form['statement'].strip().lower()

    result = "News Not Found in Dataset"

    for news in news_dataset:
        if news["statement"].lower() == user_statement:
            result = news["label"]
            break

    return render_template(
        'result.html',
        statement=request.form['statement'],
        result=result
    )


if __name__ == '__main__':
    app.run(debug=True)