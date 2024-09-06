
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Factorial of 9, since all even digits are multiplied together
    n_fact = 9
    # Base case, if the last digit is 0, return 0
    if n % 10 == 0:
        return 0
    # Iterate through the digits, multiplying the odd digits together
    for i in range(len(str(n)) - 1):
        n_fact = n_fact * 10
        n_digits = str(n)[i+1:]
        for j in range(1, len(n_digits)):
            n_digits = n_digits[:j] + str(n_digits[j]) + n_digits[j+1:]
        n = int(n_digits)
        n_fact //= 10
    return n_fact
