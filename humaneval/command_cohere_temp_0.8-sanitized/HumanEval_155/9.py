import random
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively."""
    count_even = 0
    count_odd = 0
    str_num = str(num)
    for char in str_num:
        if char == 'even':
            count_even += 1
        elif char == 'odd':
            count_odd += 1
    return (count_even, count_odd)