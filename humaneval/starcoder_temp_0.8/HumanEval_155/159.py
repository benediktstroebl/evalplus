
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if not isinstance(num, int):
        raise TypeError("num must be an integer.")

    even_count = sum(map(lambda n: n % 2 == 0, map(int, str(abs(num)))))
    odd_count = sum(map(lambda n: n % 2 == 1, map(int, str(abs(num)))))

    return (even_count, odd_count)

