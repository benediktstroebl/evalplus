def even_odd_count(num):
    if num == 0:
        return (0, 0)
    count_even = 0
    count_odd = 0
    num_str = str(num)
    for char in num_str:
        if char == '0' or char == '2' or char == '4' or char == '6' or char == '8' or char == '1' or char == '3' or char == '5' or char == '7' or char == '9':
            if char % 2 == 0:
                count_even += 1
            else:
                count_odd += 1
    return (count_even, count_odd)