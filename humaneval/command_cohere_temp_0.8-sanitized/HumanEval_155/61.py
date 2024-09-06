def even_odd_count(num):
    count_even = 0
    count_odd = 0
    num_str = str(num)
    for char in num_str:
        if char != ' ':
            if char <= '9' and int(char) % 2 == 0:
                count_even += 1
            elif char <= '9' and int(char) % 2 != 0:
                count_odd += 1
    return (count_even, count_odd)