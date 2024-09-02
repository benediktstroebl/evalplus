
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Store each digit in its own variable
    digits = []
    while n > 0:
        digit = n % 10
        n //= 10
        digits.append(digit)
    # Check if all digits are even
    if all(d == '0' or d == '1' for d in digits):
        return 0
    # Perform calculation
    for i in range(len(digits)):
        product = 0
        for j in range(i, len(digits)):
            product *= digits[j]
        digits.append(product)
    return digits[0]
