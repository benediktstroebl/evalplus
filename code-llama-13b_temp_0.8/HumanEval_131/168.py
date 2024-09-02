
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """

    def is_odd(num):
        return num % 2 == 1

    def is_even(num):
        return num % 2 == 0

    def mult_odd_digits(n):
        if n < 10:
            return n if is_odd(n) else 0
        else:
            if is_odd(n % 10):
                return n % 10 * mult_odd_digits(n // 10)
            else:
                return mult_odd_digits(n // 10)
    return mult_odd_digits(n)

