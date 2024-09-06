def even_odd_count(num):
    res = str(num)
    count_even = 0
    count_odd = 0
    for char in res:
        if char != ' ':
            if int(char) % 2 == 0:
                count_even += 1
            else:
                count_odd += 1
    return (count_even, count_odd)