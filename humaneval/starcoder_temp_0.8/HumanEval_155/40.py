
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    count_even = 0
    count_odd = 0
    if num < 0:
        num *= -1
    while num:
        count_odd += num % 10
        num = num // 10
    while num_odd:
        count_even += num_odd % 10
        num_odd = num_odd // 10
    return count_even, count_odd
