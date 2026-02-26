// Define o pino do LED (O pino 13 já tem o LED embutido na placa)
const int pinoLED = 8;
char sinalRecebido;

void setup() {
  // Inicia a comunicação serial na mesma velocidade do Python
  Serial.begin(9600);
  
  // Configura o pino do LED como saída
  pinMode(pinoLED, OUTPUT);
  
  // Garante que o LED comece desligado
  digitalWrite(pinoLED, LOW);
}

void loop() {
  // Verifica se tem alguma mensagem chegando pela porta USB
  if (Serial.available() > 0) {
    
    // Lê o caractere que o Python enviou
    sinalRecebido = Serial.read();
    
    // Se o Python mandou '1', liga o LED
    if (sinalRecebido == '1') {
      digitalWrite(pinoLED, HIGH);
    }
    // Se o Python mandou '0', desliga o LED
    else if (sinalRecebido == '0') {
      digitalWrite(pinoLED, LOW);
    }
  }
}