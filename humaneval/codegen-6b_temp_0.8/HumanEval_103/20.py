
def rounded_avg(n, m):
    """You are given two positive integers n and m, and your task is to compute the
    average of the integers from n through m (including n and m). 
    Round the answer to the nearest integer and convert that to binary.
    If n is greater than m, return -1.
    Example:
    rounded_avg(1, 5) => "0b11"
    rounded_avg(7, 5) => -1
    rounded_avg(10, 20) => "0b1111"
    rounded_avg(20, 33) => "0b11010"
    """
    
    # convert n and m to binary
    biN = '{0:b}'.format(n)
    biM = '{0:b}'.format(m)
    lenBinN = len(biN)
    lenBinM = len(biM)
    
    # check if n > m
    if n > m:
        return -1
    
    # otherwise, compute the number of digits in each
    numDitsN = lenBinN - len(biN.rstrip('0'))
    numDitsM = lenBinM - len(biM.rstrip('0'))
    
    # start from the end and add to the other digits
    fSum = 0
    for i in range(numDitsM, numDitsN + 1):
        fSum += int(biN[-i])   
    
    # Rounds the average to the nearest integer
    return '{0:b}'.format(int(fSum/numDitsN))

