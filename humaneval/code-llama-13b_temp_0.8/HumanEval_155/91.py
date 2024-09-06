
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    count = {"even": 0, "odd": 0}
    if num == 0:
        return 0, 0

    if num < 0:
        num *= -1

    while num > 0:
        if num % 10 == 0:
            count["even"] += 1
        else:
            count["odd"] += 1
        num = num // 10

    return count["even"], count["odd"]

