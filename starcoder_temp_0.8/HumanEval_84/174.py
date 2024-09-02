
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
    binary_string = str(bin(N))
    print(binary_string)
    binary_list = binary_string.split("b")
    print(binary_list)
    binary_list.pop(0)
    print(binary_list)
    print(binary_list[0])
    sum = 0
    for char in binary_list[0]:
        sum += int(char)
    return sum
