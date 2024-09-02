
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """


    # is digit even?
    is_even = lambda x: (x % 2) == 0

    # is digit odd?
    is_odd = lambda x: (x % 2) != 0

    # get count of even digits
    even_count = len(filter(is_even, map(int, str(num))))

    # get count of odd digits
    odd_count = len(filter(is_odd, map(int, str(num))))

    return (even_count, odd_count)

