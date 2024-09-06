def even_odd_count(num):
    """Return number of even and odd digits in num."""
    num_str = str(num)
    even = odd = 0
    for char in num_str:
        if char > "9":
            continue
        if int(char) % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd