
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
    sum = 0
    for num in N:
        sum += num
    result = '1'
    while sum != 0:
        if sum >= 10000:
            result = result + '10000'
            sum -= 10000
            while sum >= 10000:
                result = result + '0000' + str(sum % 10000)
                sum = sum // 10000
        else:
            result = result + str(sum % 10000)
            sum = sum // 10000
    return result
