def even_odd_count(num):
    if not isinstance(num, int):
        return "Input should be an integer"
    count_even = 0
    count_odd = 0
    str_num = str(num)
    for char in str_num:
        if char <= '9' and char >= '0':
            if int(char) % 2 == 0:
                count_even += 1
            else:
                count_odd += 1
    return (count_even, count_odd)