int analogPin = A0; 
float V2;  // Cambié a 'float' para almacenar valores decimales.
int dt = 500; 
int analogVal; 

void setup() { 
  // put your setup code here, to run once: 
  pinMode(13, INPUT); 
  Serial.begin(9600); 
} 

void loop() { 
  // put your main code here, to run repeatedly: 
  analogVal = analogRead(analogPin); 
  V2 = (5.0 * analogVal) / 1023.0; // Aseguramos que se haga una división en punto flotante
  Serial.println(V2); 
  delay(dt);
}
