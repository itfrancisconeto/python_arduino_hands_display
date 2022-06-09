
char cmd;
int disp_pinos[8] = {3, 2, 9, 7, 6, 4, 5, 8};

void setup() {
  Serial.begin(9600);
  for(int i=0; i<8; i++){
    pinMode(disp_pinos[i], OUTPUT);
  }
}

void loop() {
  cmd = Serial.read();
  if (cmd == '5') 
  {
    digitalWrite(3, HIGH);
    digitalWrite(2, LOW);
    digitalWrite(9, HIGH);
    digitalWrite(7, HIGH);
    digitalWrite(6, LOW);
    digitalWrite(4, HIGH);
    digitalWrite(5, HIGH);
    digitalWrite(8, LOW);
  }
  else if (cmd == '4')
  {
    digitalWrite(3, LOW);
    digitalWrite(2, HIGH);
    digitalWrite(9, HIGH);
    digitalWrite(7, LOW);
    digitalWrite(6, LOW);
    digitalWrite(4, HIGH);
    digitalWrite(5, HIGH);
    digitalWrite(8, LOW);
  }
  else if (cmd == '3')
  {
    digitalWrite(3, HIGH);
    digitalWrite(2, HIGH);
    digitalWrite(9, HIGH);
    digitalWrite(7, HIGH);
    digitalWrite(6, LOW);
    digitalWrite(4, LOW);
    digitalWrite(5, HIGH);
    digitalWrite(8, LOW);
  }
  else if (cmd == '2')
  {
    digitalWrite(3, HIGH);
    digitalWrite(2, HIGH);
    digitalWrite(9, LOW);
    digitalWrite(7, HIGH);
    digitalWrite(6, HIGH);
    digitalWrite(4, LOW);
    digitalWrite(5, HIGH);
    digitalWrite(8, LOW);
  }
  else if (cmd == '1')
  {
    digitalWrite(3, LOW);
    digitalWrite(2, HIGH);
    digitalWrite(9, HIGH);
    digitalWrite(7, LOW);
    digitalWrite(6, LOW);
    digitalWrite(4, LOW);
    digitalWrite(5, LOW);
    digitalWrite(8, LOW);
  }
  else if (cmd == '0')
  {
    digitalWrite(3, HIGH);
    digitalWrite(2, HIGH);
    digitalWrite(9, HIGH);
    digitalWrite(7, HIGH);
    digitalWrite(6, HIGH);
    digitalWrite(4, HIGH);
    digitalWrite(5, LOW);
    digitalWrite(8, LOW);
  }
  else if (cmd == 'd') 
  {
    digitalWrite(3, LOW);
    digitalWrite(2, LOW);
    digitalWrite(9, LOW);
    digitalWrite(7, LOW);
    digitalWrite(6, LOW);
    digitalWrite(4, LOW);
    digitalWrite(5, LOW);
    digitalWrite(8, LOW);
  }
}
