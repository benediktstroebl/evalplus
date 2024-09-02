
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
    # N.is_integer() checks if the variable N is an integer and returns True if it is.
    # If the variable N is not an integer, the code inside the if statement will never execute.
    if N.is_integer():
        N = N.evalf()  # converts the float to an integer

        # Initialize the result string with "0"
        result_str = "0"

        # Iterate over each digit in N and update the result string
        for i in range(10):
            if N % 10 == i:
                result_str += str(N // 10)
            N //= 10

        # Trim leading zeros from the result string
        result_str = result_str[:-1]

        return result_str
    else:
        return "0"  # if N is not an integer, return "0"

solve(int(input()))