
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    digits = str(num)
    result = []
    for i, d in enumerate(digits):
        if i % 2 == 0:
            result.append(i)
        else:
            result.append(i + 1)
    return result
