def even_odd_count(num):
    """Return a tuple with counts of even and odd digits."""
    count = 0
    num_str = str(num)
    for char in num_str:
        if char > '9':
            continue
        elif char % 2 == 0:
            count += 1
        else:
            count -= 1
    return count, abs(count)