def sum_squares(lst):
    result = 0
    for i, num in enumerate(lst):
        if not isinstance(num, int):
            raise TypeError("Input list must contain only integers.")
        if i % 3 == 0:
            num **= 2
        elif i % 4 == 0 and i % 3 != 0:
            num **= 3
        result += num
    return result