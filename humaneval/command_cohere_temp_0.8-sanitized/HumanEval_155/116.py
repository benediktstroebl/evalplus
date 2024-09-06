def even_odd_count(num):
    if not isinstance(num, int):
        raise TypeError("Input must be an integer")
    num_str = str(num)
    count_even = 0
    count_odd = 0
    for char in num_str:
        if char != '0' and int(char) % 2 == 0:
            count_even += 1
        elif char != '0' and int(char) % 2 != 0:
            count_odd += 1
    return (count_even, count_odd)