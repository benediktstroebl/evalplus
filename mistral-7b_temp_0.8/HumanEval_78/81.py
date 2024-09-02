
def hex_key(num):
    """You have been tasked to write a function that receives 
    a hexadecimal number as a string and counts the number of hexadecimal 
    digits that are primes (prime number, or a prime, is a natural number 
    greater than 1 that is not a product of two smaller natural numbers).
    Hexadecimal digits are 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F.
    Prime numbers are 2, 3, 5, 7, 11, 13, 17,...
    So you have to determine a number of the following digits: 2, 3, 5, 7, 
    B (=decimal 11), D (=decimal 13).
    Note: you may assume the input is always correct or empty string, 
    and symbols A,B,C,D,E,F are always uppercase.
    Examples:
    For num = "AB" the output should be 1.
    For num = "1077E" the output should be 2.
    For num = "ABED1A33" the output should be 4.
    For num = "123456789ABCDEF0" the output should be 6.
    For num = "2020" the output should be 2.
    """
    d1= {'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
    d2= {'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    l = []
    for i in num:
        if i in d1:
            l.append(d1[i])
        elif i in d2:
            l.append(int(i))
    m = []
    for i in l:
        if i==1 or i==2 or i==5 or i==7 or i==11 or i==13:
            m.append(1)
    return sum(m)
    # return sum([1 if i == 2 or i == 3 or i == 5 or i == 7 or i == 11 or i == 13 or i == 17 or i == 19 or i == 23 or i == 29 or i == 31 or i == 3
