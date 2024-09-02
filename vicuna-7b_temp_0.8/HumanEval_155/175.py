
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if num < 0:
        return -1
    elif not str(num).isdigit():
        return -1
    else:
        count_even = 0
        count_odd = 0
        for i, c in enumerate(str(num)):
            if c in '048':
                count_odd += 1
            elif c in '369':
                count_even += 1
        return (count_even, count_odd)
