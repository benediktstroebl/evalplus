
def solve(N):
    """Given a positive integer N, return the total sum of its digits in binary.
    
    Example
        For N = 1000, the sum of digits will be 1 the output should be "1".
        For N = 150, the sum of digits will be 6 the output should be "110".
        For N = 147, the sum of digits will be 12 the output should be "1100".
    
    Variables:
        @N integer
             Constraints: 0 ≤ N ≤ 10000.
    Output:
         a string of binary number
    """
    #print(N)
    num = list(str(N))
    num = list(map(int, num))
    print(num)
    print(bin(num[0]))
    s = bin(num[0])
    #print(s)
    s = str(s)
    #print(s)
    s = s[2:]
    print(s)
    sum = 0
    for i in s:
        sum = sum + int(i)
    return bin(sum)
    #return sum
    
    

