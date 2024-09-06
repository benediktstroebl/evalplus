def even_odd_count(num):
    if isinstance(num, int): 
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
    else:
        return "Error: Please provide an integer."