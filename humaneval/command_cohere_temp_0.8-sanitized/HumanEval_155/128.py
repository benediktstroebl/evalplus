def even_odd_count(num):
    res = str(num)
    count_even = count_odd = 0
    for char in res:
        if char > '9':
            if char % 2 == 0:
                count_even += 1
            else:
                count_odd += 1
        else:
            count_even += 1
    return (count_even, count_odd)