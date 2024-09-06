
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

    if not isinstance(num, int):
        raise ValueError('{} is not an integer.'.format(num))

    num_str = str(num)
    evens = sum([1 if i % 2 == 0 else 0 for i in map(int, num_str)])
    odds = sum([1 if i % 2 == 1 else 0 for i in map(int, num_str)])

    return (evens, odds)

