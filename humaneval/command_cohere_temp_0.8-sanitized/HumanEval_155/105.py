def even_odd_count(num):
    if num == 0:
        return (0, 0)
    num_str = str(num)
    even_count = 0
    odd_count = 0
    for char in num_str:
        if char % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count