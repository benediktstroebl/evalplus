def double_the_difference(lst):
    odd_and_valid = []   
    for num in lst:
        if isinstance(num, int) and num > 0:
            odd_and_valid.append(num)
    return sum(x * x for x in odd_and_valid)