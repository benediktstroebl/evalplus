
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    ten_power = 10
    even_count = 0
    odd_count = 0
    if num < 0:
        num *= -1
    while num:
        digit = num % ten_power
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        num //= ten_power
    return even_count, odd_count

