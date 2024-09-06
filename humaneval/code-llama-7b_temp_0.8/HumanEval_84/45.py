
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
    binary_number = bin(N)
    binary_list = []
    for i in binary_number:
        if i == 'b':
            continue
        else:
            binary_list.append(i)
    total = 0
    for i in binary_list:
        total += int(i)
    return str(total)
