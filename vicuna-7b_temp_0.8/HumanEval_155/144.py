
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    # Convert number to string and then to int
    n = int(str(num))
    digits = [0, 0]
    for i in range(10):
        digits[num % 10 == i] = 1
    return digits
