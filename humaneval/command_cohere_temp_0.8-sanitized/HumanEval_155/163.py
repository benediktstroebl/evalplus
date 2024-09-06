def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively."""
    result = num >= 0
    if result:
        num = str(num)
    else:
        num = str(-num)
    count_ev = 0
    count_od = 0
    for char in num:
        if char == '0' or char == '2' or char == '4' or char == '6' or char == '8':
            count_ev += 1
        elif char == '1' or char == '3' or char == '5' or char == '7' or char == '9':
            count_od += 1
    if not result:
        count_ev = -count_ev
    return (count_ev, count_od)