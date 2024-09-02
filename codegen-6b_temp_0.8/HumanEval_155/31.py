
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    count_one = 0
    count_two = 0
    if num < 0:
        num = -num
    while num:
        if num % 2:
            count_one += 1
        else:
            count_two += 1
        num //= 10
    return (count_one, count_two)

