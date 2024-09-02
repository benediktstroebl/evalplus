
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    counter = [0] * 2
    for n in str(num):
        if n in ["0", "2", "4", "6", "8"]:
            counter[0] += 1
        else:
            counter[1] += 1
    return tuple(counter)
