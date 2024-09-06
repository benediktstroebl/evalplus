
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

    # The assert statement is provided for your convenience. It checks if your
    # solution is valid by running it with several inputs and comparing the
    # output to the expected value.

    # Add your code here!
    assert even_odd_count(22) == (2, 0)
    assert even_odd_count(123) == (1, 2)
    assert even_odd_count(-12345) == (1, 4)
    assert even_odd_count(-1) == (0, 1)

    even_digits = 0
    odd_digits = 0
    number = abs(num)
    while number != 0:
        digit = number % 10
        if digit % 2 == 0:
            even_digits += 1
        else:
            odd_digits += 1
        number = number // 10
    return (even_digits, odd_digits)

