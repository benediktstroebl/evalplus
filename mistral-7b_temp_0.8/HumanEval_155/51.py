
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    number_of_even = 0
    number_of_odd = 0

    for digit in str(num):
        if digit.isdigit():
            if int(digit) % 2 == 0:
                number_of_even += 1
            else:
                number_of_odd += 1

    return (number_of_even, number_of_odd)
