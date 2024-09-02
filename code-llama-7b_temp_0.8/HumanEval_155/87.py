
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

    # 1. Handle Invalid Input
    if not isinstance(num, int):
        raise TypeError('"num" must be an integer.')

    # 2. Write code here
    count_even = 0
    count_odd = 0
    temp_string = str(num)
    for char in temp_string:
        if char % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
    return (count_even, count_odd)

