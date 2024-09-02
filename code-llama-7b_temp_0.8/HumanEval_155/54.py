
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    number_of_even_digits = 0
    number_of_odd_digits = 0
    number = abs(num)
    while number > 0:
        current_digit = number % 10
        if current_digit % 2 == 0:
            number_of_even_digits += 1
        else:
            number_of_odd_digits += 1
        number = number // 10
    return number_of_even_digits, number_of_odd_digits

