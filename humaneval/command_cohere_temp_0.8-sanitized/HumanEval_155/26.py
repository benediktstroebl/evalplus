def even_odd_count(num):
    even, odd = 0, 0
    str_num = str(num)
    for char in str_num:
        if char <= '9' and char >= '0':
            if int(char) % 2 == 0:
                even += 1
            else:
                odd += 1
    return (even, odd)