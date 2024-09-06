
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    # odd digits are the ones that end with odd numbers
    # and even digits are the ones that end with even numbers
    # so there are two possibilities
    # all numbers will be odd or all numbers will be even
    # that's why we have two cases.
    if num % 2 == 0:
        # all numbers are even
        return (len(str(num)), 0)
    else:
        # all numbers are odd
        return (0, len(str(num)))

    # you could also do
    # return (str(num).count("2"), str(num).count("3") + str(num).count("5") + str(num).count("7"))

