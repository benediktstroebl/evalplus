
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    count = (0, 0)
    if num == 0:
        return count
    elif num < 0:
        num = num * (-1)
    for i in str(num):
        if int(i) % 2 == 0:
            count = (count[0] + 1, count[1])
        else:
            count = (count[0], count[1] + 1)
    return count

