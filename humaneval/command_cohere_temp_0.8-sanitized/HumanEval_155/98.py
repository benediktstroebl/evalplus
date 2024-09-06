def even_odd_count(num):
    """Return a tuple with counts of even and odd digits."""
    count = 0
    num_str = str(abs(num))
    for char in num_str:
        if char > '9':
            continue
        if char % 2 == 0:
            count += 1
    return (count, num_str.count('1')) if num_str.count('1') > 0 else (count, 0)