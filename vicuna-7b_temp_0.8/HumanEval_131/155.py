
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Take the absolute value of n to handle negative values
    n = abs(n)
    # Handle the case where all digits are even
    if sum(map(lambda x: x % 2 == 0, str(n))) == 0:
        return 0
    # Convert the number to a string and convert each digit to a separate variable
    digits = str(n)
    digits = [int(d) for d in digits]
    # Initialize a counter variable to keep track of the odd digits
    odd_count = 0
    # Iterate over the digits from the rightmost digit to the leftmost digit
    for i in range(len(digits) - 1, 0, -1):
        # If the current digit is odd, increment the counter
        if digits[i] % 2 == 1:
            odd_count += digits[i]
        # If the current digit is the leftmost digit, update the leftmost digit
        if i == 0:
            digits[0] = odd_count
            odd_count = 1
    return odd_count
