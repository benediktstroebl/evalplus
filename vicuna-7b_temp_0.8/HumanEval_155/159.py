
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if num > 0:
        # If number is positive
        digit = 0
        count = 1
        while num > 0:
            digit = (digit * 10) + (num % 10)
            num = (num // 10)
            count += 1
        return (count % 2, count // 2)
    else:
        # If number is negative
        digit = 0
        count = 1
        while num > 0:
            digit = (digit * 10) + (num % 10)
            num = (num // 10)
            count += 1
        return (count % 2, count // 2)