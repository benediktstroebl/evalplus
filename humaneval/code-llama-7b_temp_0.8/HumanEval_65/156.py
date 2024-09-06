
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """

    digits = []
    rev_digits = []
    count = 0
    while x > 0:
        digits.append(x % 10)
        x = x // 10
        count += 1
    while count > 0:
        rev_digits.append(digits.pop())
        count -= 1

    if shift <= count:
        out = ""
        for i in range(shift, count + 1):
            out += str(rev_digits[i - 1])
        for j in range(shift):
            out += str(digits[count - j - 1])
        return out
    else:
        return "".join(str(digit) for digit in rev_digits)

