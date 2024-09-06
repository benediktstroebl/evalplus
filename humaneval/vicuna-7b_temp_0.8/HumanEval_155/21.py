
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    # first find the sum of digits
    digits = sum(str(num) for num in range(10))
    # check if the number is positive or negative
    if num >= 0:
        odd_count = 0
        for i in range(10):
            if (num // i) % 2 == 1:
                odd_count += 1
        return digits, odd_count
    else:
        digits, odd_count = 0, 0
        for i in range(10):
            if (num // i) % 2 == 1:
                odd_count += 1
        for i in range(10):
            if (num // i) % 2 == 0:
                digits += 1
        return digits, odd_count

