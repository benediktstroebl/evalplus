def even_odd_count(num):
    res = str(num).split("")
    even, odd = 0, 0
    for x in res:
        if x[0] % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd