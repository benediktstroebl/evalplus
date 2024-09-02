
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if not num:
        return (0, 0)

    num_str = str(num)
    even = 0
    odd = 0

    for digit in num_str:
        digit = int(digit)
        if digit % 2:
            odd += 1
        else:
            even += 1

    return (even, odd)
