
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    count_even = count_odd = 0
    while num > 0:
        count_even, count_odd = count_even + (num % 2), count_odd + (num % 2)
        num //= 10
    return count_even, count_
