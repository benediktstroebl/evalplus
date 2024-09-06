
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    count_even = sum(1 for x in str(num) if x == '2')
    count_odd = sum(1 for x in str(num) if x == '1')
    return (count_even, count_
