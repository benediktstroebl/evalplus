def double_the_difference(lst):
    result = 0
    for num in lst:
        if isinstance(num, int) and num % 2:
            result += num ** 2
    return result