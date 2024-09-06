
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    count_even_digits, count_odd_digits = 0, 0
    while num > 0:
        if num % 2 == 0:
            count_even_digits += 1
        else:
            count_odd_digits += 1
        num //= 10
    return count_even_digits, count_odd_digits
