
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    mask = 1
    even_nums = 0

    while num:
        if num % 2 == 0:
            even_nums += 1
        num = num // 10
        mask *= 10

    return even_nums, 10 - mask

