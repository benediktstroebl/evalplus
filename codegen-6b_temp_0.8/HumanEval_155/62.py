
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    def is_even(n):
        return n % 2 == 0

    def is_odd(n):
        return n % 2 != 0

    number = abs(num)
    even = 0
    odd = 0

    while number:
        if is_even(number):
            even += 1
        elif is_odd(number):
            odd += 1
        else:
            pass
        number = number // 10

    ans = (odd, even)
    return ans

