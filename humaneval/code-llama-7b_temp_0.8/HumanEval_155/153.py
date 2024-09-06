
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

    # Declare a variable to hold the count of the number of even digits.
    even_digits_count = 0

    # Declare a variable to hold the count of the number of odd digits.
    odd_digits_count = 0

    # 1) Iterate through the digits of num.
    # 2) If the digit is even, increment even_digits_count.
    # 3) Else, increment odd_digits_count.
    for digit in str(num):
        if int(digit) % 2 == 0:
            even_digits_count += 1
        else:
            odd_digits_count += 1

    return (even_digits_count, odd_digits_count)

