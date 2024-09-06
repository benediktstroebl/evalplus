def even_odd_count(num):
    if num == 0:
        return (0, 0)
    count_even = 0
    count_odd = 0
    temp = str(num)
    for i in temp:
        if i == '0' or i == '6' or i == '8' or i == '4':
            count_even += 1
        elif i == '1' or i == '3' or i == '5' or i == '7' or i == '9':
            count_odd += 1
    return (count_even, count_odd)