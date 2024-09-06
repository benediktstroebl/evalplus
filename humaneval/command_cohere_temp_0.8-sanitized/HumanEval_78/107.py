import math
def hex_key(num):
    prime_digits = {'0':0,'1':0,'2':1,'3':1,'4':0,'5':1,'6':0,'7':1,'8':0,'9':0,
                    'A':1,'B':1,'C':1,'D':1,'E':1,'F':1}
    return sum(prime_digits[d] for d in num if d in prime_digits)