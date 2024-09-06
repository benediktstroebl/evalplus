def even_odd_count(num):
    count = 0
    for digit in str(num):
        if int(digit) % 2 == 0:
            count += 1
        elif int(digit) % 2 != 0:
            count += 1
    return count