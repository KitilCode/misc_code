#some variables and data sets to refrence
roman_ones = {0:'',1:'I',2:'II',3:'III',4:'IV',5:'V',6:'VI', 7:'VII', 8:'VIII', 9:'IX'}
roman_tens = {9: 'XC'}
roman_hundreds = {9:'CM'}
roman_thousands= {1:'M',2:'MM',3:'MMM'}
for x in range(9):
    roman_tens[x] = roman_ones[x].replace('I','X').replace('V','L')
for x in range(9):
    roman_hundreds[x] = roman_ones[x].replace('I','C').replace('V','D')
call_this = {1:roman_ones,2:roman_tens,3:roman_hundreds,4:roman_thousands}

def digit_to_roman(n):
    n = str(n)
    if len(n) == 0:
        return ''
    else:
        return call_this[len(n)][int(n[0])] + digit_to_roman(n[1:])
