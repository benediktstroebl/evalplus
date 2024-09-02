
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

    if num == 0:
        return (0, 0)

    n = abs(num)

    count_even = 0
    count_odd = 0

    while n > 0:
        n, remainder = divmod(n, 10)
        if remainder % 2 == 0:
            count_even += 1
        else:
            count_odd += 1

    return count_even, count_odd
