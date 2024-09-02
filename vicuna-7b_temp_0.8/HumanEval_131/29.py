
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    digits = [int(d) for d in str(n) if d.isdigit()]
    n = [0] * 10
    for i in range(len(digits)):
        n[digits[i]] += digits[i+1] if digits[i] == 1 else 0
    for i in range(len(n)):
        if n[i] % 2 == 1:
            return n[i]
    return 0
