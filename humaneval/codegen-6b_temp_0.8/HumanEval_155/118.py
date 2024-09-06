
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    def get_digits(num, digit_count):
        while num > 0 and digit_count > 0:
            digit = int(num % 10)
            if digit % 2 == 0:
                digit_count -= 1
            num //= 10
        return digit_count

    even, odd = get_digits(num, 2), get_digits(num, 1)
    return (even, odd)

