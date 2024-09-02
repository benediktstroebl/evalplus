
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    return (str(num).count("0") + str(num).count("1") + str(num).count("2") + str(num).count("3") + str(num).count("4") + str(num).count("5") + str(num).count("6") + str(num).count("7") + str(num).count("8") + str(num).count("9"), str(num).count("1") + str(num).count("3") + str(num).count("5") + str(num).count("7") + str(num).count("9"))
