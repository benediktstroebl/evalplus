
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if num < 0:
        return even_odd_count(-num)

    if num == 0:
        return 0, 1

    length = len(str(abs(num)))
    is_even = length % 2 == 0
    return is_even, length

