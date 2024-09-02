
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
        digit = sum % 10
        sum = (sum // 10) * 10 + num
        if digit != num:
            print("Not a digit sum")
            return
    result = str(sum)
    while len(result) < 4:
        if sum % 2 != 0:
            result = "1" + result
        else:
            result = "0" + result
    return result