
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

    #initializing values
    n = int(n)
    m = int(m)
    sum = 0
    count = 0
    new_n = 0

    #checking if n is greater than m
    if m > n:
        return -1

    #iterating n from n to m
    for i in range(n, m+1):
        sum += i
        count += 1

    #converting the integer sum to binary
    #new_n = bin(sum)[2:]
    #print(new_n)
    new_n = format(sum, 'b')

    #checking if count is odd or even
    if count % 2 == 0:
        #print(new_n[len(new_n)//2:])
        new_n = new_n[len(new_n)//2:]

    #print(new_n)

    return new_n

