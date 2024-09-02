
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    def is_even(num):
        return num % 2 == 0

    def is_odd(num):
        return num % 2 != 0

    even_count = 0
    odd_count = 0
    for digit in str(num):
        if is_even(int(digit)):
            even_count += 1
        elif is_odd(int(digit)):
            odd_count += 1
        else:
            continue
    return even_count, odd_count

