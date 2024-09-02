
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if not isinstance(num, int):
        return False

    count = [0, 0]
    digits = str(num).split()

    for digit in digits:
        if digit % 2 == 0:
            count[0] += 1
        else:
            count[1] += 1

    return tuple(count)
