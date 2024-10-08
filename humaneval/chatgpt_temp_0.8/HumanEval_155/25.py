def even_odd_count(num):
    even_count = 0
    odd_count = 0
    for digit in str(abs(num)):
        if int(digit) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    if num < 0:
        return (0, 0)  # return (0, 0) if num is negative
    else:
        return (even_count, odd_count)
