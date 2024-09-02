
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

    return (num.count("0") + num.count("2") + num.count("4") + num.count("6") + num.count("8"),
            num.count("1") + num.count("3") + num.count("5") + num.count("7") + num.count("9"))

