def choose_num(x, y):
    max_even = -1
    target = x if x % 2 == 0 else y
    for num in range(max(x, y), min(x, y) - 1, -1):
        if num % 2 == 0:
            max_even = num
            break
    return max_even if max_even in range(x, y + 1) else -1