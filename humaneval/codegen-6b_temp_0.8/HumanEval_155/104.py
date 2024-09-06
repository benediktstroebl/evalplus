
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if num < 0:
        return even_odd_count(-num)
    arr = []
    while num > 0:
        if num % 2 == 0:
            arr.append(0)
        else:
            arr.append(1)
        num /= 10
    return tuple(arr)

