const newsDataset = [
    {
        statement: "India's Chandrayaan-3 successfully landed near the Moon's south pole on August 23, 2023",
        label: "True"
    },
    {
        statement: "India hosted the G20 Leaders Summit in New Delhi in 2023",
        label: "True"
    },
    {
        statement: "NASA's Perseverance rover is exploring Mars",
        label: "True"
    },
    {
        statement: "The World Health Organization declared COVID-19 a pandemic in March 2020",
        label: "True"
    },
    {
        statement: "The James Webb Space Telescope released its first full-color scientific images in 2022",
        label: "True"
    },
    {
        statement: "COVID-19 vaccines contain microchips used to track people",
        label: "Fake"
    },
    {
        statement: "5G mobile towers spread coronavirus through radio waves",
        label: "Fake"
    },
    {
        statement: "NASA confirmed that Earth will experience six days of darkness next month",
        label: "Fake"
    },
    {
        statement: "Vaccines cause autism in children",
        label: "Fake"
    },
    {
        statement: "The Earth is flat and governments are hiding the truth",
        label: "Fake"
    }
];

function detectNews() {

    const input = document
        .getElementById("statement")
        .value
        .trim()
        .toLowerCase();

    const resultDiv = document.getElementById("result");

    let result = null;

    newsDataset.forEach(news => {
        if(news.statement.toLowerCase() === input){
            result = news.label;
        }
    });

    resultDiv.className = "result-box";

    if(result === "True"){
        resultDiv.classList.add("true");
        resultDiv.innerHTML =
            "✅ VERIFIED NEWS";
    }
    else if(result === "Fake"){
        resultDiv.classList.add("fake");
        resultDiv.innerHTML =
            "❌ FAKE NEWS DETECTED";
    }
    else{
        resultDiv.classList.add("notfound");
        resultDiv.innerHTML =
            "⚠ News not found in dataset";
    }

    resultDiv.style.display = "block";
}