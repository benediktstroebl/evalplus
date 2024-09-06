def even_odd_count(num):
    if num == 0:
        return (0, 0)
    num_str = str(num)
    count_ev = 0
    count_od = 0
    for char in num_str:
        if char == '0' or char == '2' or char == '4' or char == '6' or char == '8':
            count_ev += 1
        elif char == '1' or char == '3' or char == '5' or char == '7' or char == '9':
            count_od += 1
    return (count_ev, count_od)