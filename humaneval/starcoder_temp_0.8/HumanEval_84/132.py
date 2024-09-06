
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

    # Convert integer to binary string
    bin_str = bin(N)
    # Remove 0b from beginning of string
    bin_str = str(bin_str)[2:]
    # Split binary string into digits
    bin_str = bin_str.split()

    # Sum each digit
    sum_digits = sum(int(bin_digit) for bin_digit in bin_str)

    return sum_digits

