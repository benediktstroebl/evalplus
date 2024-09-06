def choose_num(x, y):
    max_even = -1
    bounds = [x, y]
    for num in range(x, y + 1):
        if num % 2 == 0 and num > max_even:
            max_even = num
    return max_even if max_even != -1 else -1