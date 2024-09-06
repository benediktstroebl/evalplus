def even_odd_count(num):
    if num == 0:
        return (0, 0)
    count_even = 0
    count_odd = 0
    temp = str(num)
    for i in temp:
        if i % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
    return (count_even, count_odd)