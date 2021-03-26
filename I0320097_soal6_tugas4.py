#Soal6

a = 4
b = 11

#A bitwise OR (|)
c = a | b
print('\n$$$$$$$$$$OR$$$$$$$$$$')
print('nilai :',a,' , binary :', format(a,'08b'))
print('nilai :',b,' , binary :', format(b,'08b'))
print('------------------------------------------ (|)')
print('nilai :',c,' , binary :', format(c,'08b'))

#B shif right (>>)
c = a >> b
print('\n$$$$$$$$$$>>$$$$$$$$$$')
print('nilai :',a,' , binary :', format(a,'08b'))
print('nilai :',b,' , binary :', format(b,'08b'))
print('---------------------------------------- (>>)')
print('nilai :',c,' , binary :', format(c,'08b'))

#C bitwise XOR (^)
c = a ^ b
print('\n$$$$$$$$$$XOR$$$$$$$$$$')
print('nilai :',a,' , binary :', format(a,'08b'))
print('nilai :',b,' , binary :', format(b,'08b'))
print('----------------------------------------- (^)')
print('nilai :',c,' , binary :', format(c,'08b'))

#D bitwise NOT (~)
c = ~a
print('\n$$$$$$$$$$NOT$$$$$$$$$$')
print('nilai :',a,' , binary :', format(a,'08b'))
print('----------------------------------------- (~)')
print('nilai :',c,' , binary :', format(c,'08b'))

#E bitwise AND (&)
c = b & a
print('\n$$$$$$$$$$AND$$$$$$$$$$')
print('nilai :',b,' , binary :', format(b,'08b'))
print('nilai :',a,' , binary :', format(a,'08b'))
print('---------------------------------------- (&)')
print('nilai :',c,' , binary :', format(c,'08b'))