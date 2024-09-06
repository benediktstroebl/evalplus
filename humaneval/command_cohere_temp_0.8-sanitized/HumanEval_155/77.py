def even_odd_count(num):
    if not isinstance(num, int):
        raise ValueError("Input must be an integer")
    if num < 0:
        return (0, 0)  # no digits in abs(num)
    num = str(abs(num))
    even, odd = 0, 0
    for digit in num:
        if digit % 2 == 0:
            even += 1
        else:
            odd += 1
    return (even, odd)