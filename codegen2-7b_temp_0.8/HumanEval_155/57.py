
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    counter = 0
    for digit in str(num):
        if digit.isdigit():
            counter += 1
    if counter % 2 == 0:
        return f"{counter} even digits", (counter - 1) / 2
    return f"{counter} odd digits", (counter - 1) / 2
