def even_odd_count(num):
    if num == 0:
        return (0, 0)
    elif num < 0:
        return (1, 1)
    else:
        digits = [int(i) for i in str(num)]
        even_count = sum(1 for digit in digits if digit % 2 == 0)
        odd_count = sum(1 for digit in digits if digit % 2 != 0)
        return (even_count, odd_count)