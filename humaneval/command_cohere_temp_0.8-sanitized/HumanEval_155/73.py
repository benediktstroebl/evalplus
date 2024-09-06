def even_odd_count(num):
    """Return number of even and odd digits in num."""
    # Convert num to str and remove any non-digit characters
    num = str(num).strip('-.')
    count_odd = count_even = 0
    for char in num:
        if char > '9':
            continue
        elif char % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
    return (count_even, count_odd)