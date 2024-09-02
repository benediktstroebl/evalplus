
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
    n = N
    # Get the digit string
    digits = str(n)
    # Split the digit string into a list of digits
    digits_list = digits.split()
    # Initialize a variable to keep track of the sum of digits
    sum = 0
    # Iterate through the digits in the list
    for i in range(len(digits_list)):
        sum = sum + int(digits_list[i])
    # Convert the sum to binary
    binary_sum = str(sum)
    # Concatenate the binary_sum with the leading zeros
    binary_sum = "0" + binary_sum
    # Check if N is a power of 2
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return binary_sum
