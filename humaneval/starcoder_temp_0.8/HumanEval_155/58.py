
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    count_even = 0
    count_odd = 0
    if num < 0:
        num = num * -1
    if num == 0:
        return 0, 0
    elif num < 10:
        if num % 2 == 0:
            count_even = count_even + 1
        else:
            count_odd = count_odd + 1
        return count_even, count_odd
    else:
        if num % 2 == 0:
            count_even = count_even + 1
        else:
            count_odd = count_odd + 1
        return even_odd_count(num//10) + (count_even, count_odd)
