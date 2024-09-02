
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # First, split x into a list of digits.
    digits = []
    while x > 0:
        # Pop digits off the end of the list to add to digits
        digits.insert(0, x % 10)
        x //= 10
    # Reverse the list of digits if shift > len(digits)
    if shift > len(digits):
        digits = list(reversed(digits))
    elif shift <= 0:
        digits = list(reversed(digits[abs(shift):]))
        # We have to do a different count if we're shifting left or right
        if shift < 0:
            shift += len(digits)
        shift %= len(digits)
    # Get the new digits by slicing the list of digits from the start to shift
    # digits and adding the digits from the end of the list.
    new_digits = digits[:shift]
    new_digits.extend(digits[shift:])
    # Turn the new digits into a number (an integer)
    n = 0
    for d in new_digits:
        n = 10 * n + d
    return str(n)
