
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    count = 0
    for digit in str(num):
        if digit.isdigit():
            count += 1
    return (count, count % 2
