
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    even = sum(int(digit) for digit in str(num) if digit.isdigit())
    odd = len(str(num)) - even
    return (even, odd)
