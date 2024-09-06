def even_odd_count(num):
    digit_count = 0
    even_count = 0

    while num:
        digit = num % 10
        even_count += digit % 2
        digit_count += 1
        num //= 10

    return (even_count, digit_count - even_count)