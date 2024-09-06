
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    num = int(num)
    even = sum(digit % 2 == 0 for digit in str(num))
    odd = sum(digit % 2 == 1 for digit in str(num))
    return (even, odd
