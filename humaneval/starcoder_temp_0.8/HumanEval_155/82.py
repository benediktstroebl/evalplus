
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if num < 0:
        raise ValueError("Num must be a positive integer")
    return (sum([int(i) for i in str(num)]), len(str(num)) - sum([int(i) for i in str(num)]))
