
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Use a loop to avoid having to use more advanced techniques
    # like binary search or the 'range' function
    # Instead, we'll use a loop to iterate through the digits of n
    # One way to implement this is to use a loop with a range of 1
    # and a modulus operation to check if we've exceeded the number n
    # This will allow us to check each digit of n as we iterate through
    # the range of 1 to n
    for i in range(1, len(str(n))):
        # If the current digit is odd, multiply it by itself
        # and add the result to the product
        product = 1
        for j in range(i, len(str(n))):
            if n % 10 > 0:
                product *= 10
            if n % 10 == 0:
                break
        if i % 2 == 1:
            result = product
        else:
            result = 0
        print(result)