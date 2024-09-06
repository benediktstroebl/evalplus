
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # If all digits are even, return 0
    if sum(map(lambda x: x % 2, str(n))) == 0:
        return 0
    else:
        # Convert the input to a list of integers
        num = int(n)
        # Loop through the digits of the number, starting with the most significant
        for i in range(len(str(num)) - 1, 0, -1):
            # If the current digit is odd, multiply it by itself and add it to the result
            result += (num // i) * i
        # Return the result
        return result
