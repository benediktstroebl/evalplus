
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if num < 0:
        num = num * -1
    count_odd = 0
    count_even = 0
    while num > 0:
        mod = num % 10
        if mod % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
        num = num // 10
    return (count_even, count_odd)
