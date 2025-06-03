// Example using Chart.js
const ctx = document.getElementById('myChart').getContext('2d');
// Replace the following data with dynamic data passed from the backend
const labels = ['Sample1', 'Sample2', 'Sample3'];
const data = [10, 20, 30];

const myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: labels,
        datasets: [{
            label: 'Load vs Deflection',
            data: data,
            backgroundColor: 'rgba(54, 162, 235, 0.6)'
        }]
    },
    options: {
        responsive: true,
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});
