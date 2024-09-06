def even_odd_count(num):
    """Return number of even and odd digits in num."""
    # Convert num to string and remove any non-digit characters
    num = str(num).strip('-.')
    even, odd = 0, 0
    for char in num:
        if char > '9':
            continue
        elif char % 2 == 0:
            even += 1
        else:
            odd += 1
    return (even, odd)