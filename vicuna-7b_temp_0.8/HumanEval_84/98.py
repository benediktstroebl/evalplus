
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
    binary_list = [str(digit) for digit in str(N).split()]
    while len(binary_list) > 0:
        while True:
            digit = binary_list[-1]
            if digit in '01':
                binary_list.pop()
                continue
            elif digit == '1':
                binary_list.pop()
                break
            else:
                break
        if len(binary_list) % 2 == 1:
            binary_list.append('1')
        else:
            binary_list.append('0')
    return ''.join(binary_list)
