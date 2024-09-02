
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
    sum_of_digits = 0
    digits = [str(d) for d in N]
    while sum_of_digits < N:
        #loop to add digits
        current_sum = sum(map(int, digits))
        if current_sum >= 2:
            digits = [str(d) for d in digits if d >= 2]
            sum_of_digits += current_sum - 1
        else:
            digits = [d for d in digits if d < 2]
            sum_of_digits += N - 1
    
    return "".join(digits)

