def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively."""
    count_even = 0
    count_odd = 0
    num_str = str(num)
    for char in num_str:
        if char > '9':
            continue
        elif char == '0':
            count_even += 1
        else:
            count_odd += 1
    return (count_even, count_odd)