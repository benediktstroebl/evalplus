
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if num == 0:
        return (0, 0)
    elif num < 0:
        return even_odd_count(-num)
    else:
        string_1 = str(num)
        new_string = ""
        odd = 0
        even = 0
        for x in string_1:
            if int(x) % 2 == 0:
                even += 1
                new_string += x
            else:
                odd += 1
                new_string += x
        return (even, odd)


