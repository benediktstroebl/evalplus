
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    assert isinstance(num, int)

    # 1. Find the digits in num
    digits = list(str(num))

    # 2. Count the even and odd digits
    even_count = sum(1 for digit in digits if int(digit) % 2 == 0)
    odd_count = sum(1 for digit in digits if int(digit) % 2!= 0)

    # 3. Return a tuple that has the count of even and odd digits
    return (even_count, odd_count)
