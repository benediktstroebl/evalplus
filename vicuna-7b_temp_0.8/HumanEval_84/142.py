
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
    number = str(N)
    sum = 0
    result = ""
    for char in number:
        if char.isdigit():
            sum += int(char) * 2
        else:
            result = sum % 2 + result
            sum = sum // 2
    return result