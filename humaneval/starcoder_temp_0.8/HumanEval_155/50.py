
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if num < 0:
        num = abs(num)
    if num == 0:
        return (0, 0)
    string = str(num)
    count_odd = 0
    count_even = 0
    for i in string:
        if int(i) % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
    return (count_even, count_odd)
