
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
    # ====================================
    # SOLUTION -------------------------
    # ====================================
    sum_of_digits = 0
    n = N
    while n > 0:
        sum_of_digits += n % 2
        n //= 2
    return bin(sum_of_digits)

    # ====================================
    # CLIENT CODE -----------------------
    # ====================================
    # print(solve(int(input())))

    # ====================================
    # PROBLEM SET 04 CODE (NAIVE) -------
    # ====================================
    N = str(N)
    digits = [int(c) for c in N]
    total = 0
    for digit in digits:
        total += digit
    total = bin(total)
    return total
