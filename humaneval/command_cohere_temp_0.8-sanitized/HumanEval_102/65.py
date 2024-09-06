def choose_num(x, y):
    max_even = -1
    # Loop through potential even integers between x and y inclusive.
    for z in range(x, y + 1):
        if z % 2 == 0 and z > max_even:
            max_even = z
    return max_even if max_even != -1 else -1