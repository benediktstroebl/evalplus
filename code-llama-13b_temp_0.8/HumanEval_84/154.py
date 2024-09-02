
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

    # Converts the integer into binary.
    binary = bin(N)
    # Splits the binary into a list.
    binary = binary.split("b")[1]
    # Splits the binary into a list.
    binary = binary.split("")
    # Adds all the elements in the binary list.
    sum = 0
    for i in binary:
        sum += int(i)
    # Converts the sum back to binary.
    sum = bin(sum)
    # Removes b and the 0b from the binary.
    sum = sum.split("b")[1]
    # Returns the binary sum.
    return sum
