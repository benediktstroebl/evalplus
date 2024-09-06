
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
    # 1. Declare the sum
    sum = 0
    # 2. create the binary representation
    binary = bin(N)
    # 3. get the digits
    digits = [x for x in str(binary)[2:]]
    # 4. sum the digits
    for digit in digits:
        sum += int(digit)
    # 5. return the sum
    return str(bin(sum))[2:]

    
    
