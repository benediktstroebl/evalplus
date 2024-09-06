def even_odd_count(num):
    if num == 0:
        return (0, 0)
    count_even = 0
    count_odd = 0
    str_num = str(num)
    for char in str_num:
        if char > '9' or char < '0':
            if char in '-'+'.':
                continue
            else:
                return (0, 0) 
        if int(char) % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
    return (count_even, count_odd)