
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # This is the recursive definition of the function
    # It uses the head of the list to represent the current state
    # and calls itself to compute the next state
    if n < 10:
        return n
    digits = [0] * (10 - len(str(n)))
    digits[0] = n % 10
    n = str(n)
    if n[1] == '1':
        digits[1] += digits[0]
    else:
        return 0
    for i in range(2, len(n)):
        if n[i] == '1':
            digits[i] += digits[i - 1]
    return digits[-1]
