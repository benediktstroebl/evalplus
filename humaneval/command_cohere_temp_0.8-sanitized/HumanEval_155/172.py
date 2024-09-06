def even_odd_count(num):
    if num == 0:
        return (0, 0)
    count_odd = 0
    count_even = 0
    num_str = str(num)
    for char in num_str:
        if char > '9' or char < '0':
            if char in '-+' :
                continue
            else:
                count_odd += 1
        else:
            if int(char) % 2 == 0:
                count_even += 1
    return (count_even, count_odd)