
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Use a list to store the remaining digits, so we can append the next digit
    # to it without modifying the input value.
    digits = [n % 10]
    remaining = n // 10
    
    # Loop through the digits, starting with the second (index 1)
    # because the first digit will always be 0.
    for i in range(1, len(digits)):
        # If the current digit is odd, multiply it with the remaining sum
        # of all the digits in the list.
        if digits[i] % 2 != 0:
            result = digits[i] * remaining
            remaining = 0
        # If we have looped through all digits and the result is not zero,
        # return the result.
        if result != 0:
            return result
        # If the current digit is even, append it to the list and reset the
        # remaining sum.
        digits.append(digits[i])
        remaining = 0
    
    # Return 0 if all digits are even.
    return 0
