const int trigPin = A10;
const int echoPin = A9;

long duracion;
int distancia;


void setup() 
{
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  
  Serial.begin(9600);
}
void loop() 
{
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  duracion = pulseIn(echoPin, HIGH);
  distancia = (duracion * 0.0345) / 2;
  
  if (digitalRead(4) == 1){
    Serial.println(distancia);
  }
  delay(300);
}
