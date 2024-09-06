
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    num_string = str(num)
    num_even = 0
    num_odd = 0
    for i in num_string:
        if int(i) % 2 == 0:
            num_even += 1
        else:
            num_odd += 1

    return num_even, num_odd
