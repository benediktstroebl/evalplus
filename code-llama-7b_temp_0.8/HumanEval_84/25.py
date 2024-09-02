
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
    
    binary = bin(N)[2:]
    binary_list = list(binary)
    result = ""
    for value in binary_list:
        result += str(value)
    print(result)

    total = 0
    for value in binary:
        total += int(value)
    print(total)

    
    total_list = list(str(total))
    total_binary = ""
    for value in total_list:
        total_binary += str(bin(int(value)))[2:]
    print(total_binary)
    result = ""
    for value in total_binary:
        result += str(value)

    return result
