
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
    digits = [str(digit) for digit in N]
    for i in range(len(digits) - 1):
        if digits[i:i + 2] == [str(int(x)), str(int(x) // 10)]:
            sum += int(digits[i]) * 10 + int(digits[i + 1])
            digits.remove(str(int(digits[i:i + 2][0])))
    return ''.join(digits)

N = int(input("Enter the number: "))
