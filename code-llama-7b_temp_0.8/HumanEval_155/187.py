
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    # Even number will be in the form of 10*even_number or 10*even_number + 1
    # Odd number will be in the form of 11*even_number + 1
    # Since 10 * even_number will be always even number and
    # 11 * even_number + 1 will be always odd number.
    # So even number is in the form of 10*even_number or 10*even_number + 1
    # So odd number is in the form of 11*even_number + 1
    even = 0
    odd = 0
    for digit in str(abs(num)):
        if int(digit) % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd

