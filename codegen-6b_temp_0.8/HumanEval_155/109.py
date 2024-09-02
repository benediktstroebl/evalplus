
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if num == 0:
        return 1, 1
    
    numDigits = 0
    numStr = str(num)
    for i in xrange(len(numStr)):
        if int(numStr[i]) % 2 == 0:
            numDigits += 1
        else:
            numDigits += 0
    
    return numDigits, len(numStr) - numDigits
    
