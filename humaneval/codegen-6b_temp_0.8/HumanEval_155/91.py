
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    numbers = str(num)
    even_digits = 0
    odd_digits = 0
    for i, c in enumerate(numbers):
        if i % 2 == 0 and int(c) % 2 == 0:
            even_digits += 1
        if i % 2 == 1 and int(c) % 2 == 1:
            odd_digits += 1
    return even_digits, odd_digits
