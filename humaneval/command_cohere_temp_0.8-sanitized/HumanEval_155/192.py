def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively."""
    num_str = str(num)
    even_count = 0
    odd_count = 0
    for char in num_str:
        if char % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count