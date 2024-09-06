
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if not isinstance(num, int):
        raise TypeError("Only integers are accepted")

    num = str(num)
    result = {
        "even": 0,
        "odd": 0
    }
    for i in num:
        if int(i) % 2 == 0:
            result["even"] += 1
        else:
            result["odd"] += 1

    return (result["even"], result["odd"])
