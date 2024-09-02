
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    count_odd = sum(1 if i % 2 else 0 for i in str(num))
    count_even = sum(1 if i % 2 else 0 for i in str(num))
    return (count_even, count_odd
