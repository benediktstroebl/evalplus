
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if num < 0:
        num = -num
    count_even = count_odd = 0
    if num == 0:
        return count_even, count_odd
    while num:
        if num & 1:
            count_odd += 1
        else:
            count_even += 1
        num >>= 1
    return count_even, count_odd
