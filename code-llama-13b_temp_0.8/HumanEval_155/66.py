
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if not isinstance(num, int):
        return "Input must be a integer"
    digits = str(num)
    evens = 0
    odds = 0
    for i in digits:
        if int(i) % 2 == 0:
            evens += 1
        else:
            odds += 1
    return evens, odds

