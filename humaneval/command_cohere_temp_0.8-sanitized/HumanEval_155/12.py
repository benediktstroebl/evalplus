def even_odd_count(num):
    if isinstance(num, int): 
        count_ev = 0
        count_od = 0
        str_num = str(num)
        for char in str_num: 
            if char <= '9' and char >= '0':
                if int(char) % 2 == 0:
                    count_ev += 1
                else:
                    count_od += 1
        return (count_ev, count_od)
    else:
        return "Incorrect argument type"