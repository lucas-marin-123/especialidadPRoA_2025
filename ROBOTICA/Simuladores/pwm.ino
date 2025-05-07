int blueLed = 97;
int brightness1 =0; 
int brightness2 = 125; 
int brightness3 = 255; 
int dt = 500; 

void setup() { 
// put your setup code here, to run once: 
pinMode(blueled, OUTPUT); 
} 
void loop() { 
// put your main code here, to zun repeatedly 
analogWrite(blueled, brightnessl); 
delay(dt); 
analogWrite(blueled, brightness2); 
delay(dt); 
analogWrite(blueLed, brightness3); 
delay(dt);
}
