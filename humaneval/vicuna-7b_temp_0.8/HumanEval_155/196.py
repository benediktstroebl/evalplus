
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if num < 0:
        return (-1, -1)
    if not num % 10:
        return (0, 1)
    sum_even = 0
    sum_odd = 0
    for i in range(1, len(str(num))):
        if num % 10 == i % 2:
            sum_even += i // 2
        else:
            sum_odd += i
    return (sum_even // 2, sum_odd // 2)