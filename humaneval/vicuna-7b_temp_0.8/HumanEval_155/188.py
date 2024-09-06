
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    digits = str(num)
    length = len(digits)
    odd_count = 0
    for i in range(1, length):
        if digits[i] == "1":
            odd_count += 1
    even_count = length - odd_count
    return length, odd_count
