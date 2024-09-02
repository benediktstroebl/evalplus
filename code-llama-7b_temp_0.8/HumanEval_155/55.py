
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    # Your code here
    if num < 0:
        return (1, 1)
    else:
        if num % 2 == 0:
            return (2, 0)
        else:
            return (1, 2)
