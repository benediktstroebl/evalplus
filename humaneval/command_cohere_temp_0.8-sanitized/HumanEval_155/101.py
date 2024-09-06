def even_odd_count(num):
    """Return a tuple that has the number of even and odd digits respectively."""
    count_even = 0
    count_odd = 0
    temp_num = abs(num)
    while temp_num != 0:
        numberOfDigits = len(str(temp_num))
        # counting even digits
        count_even += temp_num % 2 == 0 and 1 or 0
        # counting odd digits
        count_odd += temp_num % 2 == 1 and 1 or 0
        temp_num //= 10
    return (count_even, count_odd)