const output = document.getElementById('output');
const startButton = document.getElementById('startButton');
let finalTranscript = '';

const SpeechRecognition = window.webkitSpeechRecognition || window.webkitSpeechRecognition;

const recognition = new SpeechRecognition();
recognition.lang = 'en-US';
recognition.interimResults = true;

startButton.addEventListener('click', () => {
    finalTranscript = '';
    output.textContent = '';
    reccognition.start();
    startButton.textContent = 'Listening...';
});
recognition.addEventListener('results', (e) => {
    const transcript = Array.from(e.result).map(result => result[0].transcript).join('');
    if (e.result[0].isFinal) {
        finalTranscript = transcript;
        output.textContent = finalTranscript;
    }
})

recognition.addEventListener('end', () => {
    startButton.textContent = 'startButton';
    recognition.start();
});

document.addEventListener('keydown', (e) => {
    if (e.key == 'Escape') {
        recognition.stop();
        startButton.textContent = 'startButton';
    }
});