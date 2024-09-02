
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if not isinstance(num, int):
        return None
    if num == 0:
        return (1, 0)
    even_count = 0
    odd_count = 0
    is_negative = num < 0
    num = abs(num)
    while num != 0:
        digit = num % 10
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        num = num // 10
    if is_negative:
        odd_count += 1
    return even_count, odd_count
