
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    evens = num // 2 if num % 2 == 0 else num // 2 + 1
    odds = num // 2 + 1 if num % 2 == 0 else num // 2
    return evens, odds

