
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if num < 0:
        raise ValueError("negative values not allowed")

    if num == 0:
        return (0, 0)

    while num!= 0:
        count = 0
        while num!= 0:
            num = num // 10
            count += 1
        if count % 2!= 0:
            odd += 1

    return
