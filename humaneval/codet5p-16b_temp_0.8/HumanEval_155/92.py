
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

    num_str = str(num)
    counter_e = 0
    counter_o = 0
    for char in num_str:
        if int(char)%2 == 0:
            counter_e += 1
        else:
            counter_o += 1
    return (counter_e, counter_o)
