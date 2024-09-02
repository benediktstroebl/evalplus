
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if num < 0:
        return -1
    while num != 0:
        if num % 2 == 0:
            if num % 3 == 0:
                return -1, -1
            if num % 2 == 1:
                num = num // 2
        else:
            if num % 2 == 0:
                num = (num - (num // 2)) // 2
            else:
                num = (num - (num // 2)) // 2
    return 0, 0
