
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
    # Write your code here
    # The following code is just for demonstration purposes.
    # You should write your own code to solve the problem.
    # The variable N is an input variable, you should store it in a variable.
    # You can use the input() function to get user input.
    # For example:
    # num = int(input("Enter a positive integer: "))
    # or
    # num = int(input("Enter a positive integer: "))
    # or
    # num = int(input("Enter a positive integer: "))
    # You should also handle edge cases and check for valid input.
    # For example, if the input is not an integer, you should raise an exception.
    
    # Here is just a sample implementation.
    # You should write your own code.
    return "1" * (N // 10) + "10"[::-1] + "1" + str(N % 10)
