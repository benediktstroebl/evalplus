
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if not isinstance(num, int):
        raise ValueError("Please input an integer")

    count = 0
    even = 0
    odd = 0

    while num > 0:
        num = int(num / 10)
        count += 1
        if num % 2 == 0:
            even += 1
        else:
            odd += 1

