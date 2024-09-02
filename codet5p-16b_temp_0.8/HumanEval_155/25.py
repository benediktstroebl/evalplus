
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

    result = list(map(lambda x: 1 if x%2 else 0, str(num)))
    return (sum(result), len(result)-sum(result))

