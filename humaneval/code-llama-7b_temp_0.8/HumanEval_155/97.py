
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    # return tuple((len(str(num)) - i) for i, c in enumerate(str(num)) if c.isdigit())
    # return tuple(sum(map(lambda n: n % 2 == 0, str(num))) for i, c in enumerate(str(num)) if c.isdigit())
    # return tuple((len(str(num)) - sum(map(lambda c: c.isdigit(), str(num)))) for i, c in enumerate(str(num)) if c.isdigit())
    return tuple(sum(map(lambda c: c.isdigit() and int(c) % 2 == 0, str(num))) for i, c in enumerate(str(num)) if c.isdigit())

