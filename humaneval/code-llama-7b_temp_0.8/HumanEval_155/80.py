
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if not num:
        return (0, 0)

    result = [0, 0]

    for n in str(abs(num)):
        if n.isdigit():
            result[int(n) % 2] += 1

    return tuple(result)

