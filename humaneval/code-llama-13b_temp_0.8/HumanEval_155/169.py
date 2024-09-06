
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if not isinstance(num, int):
        raise TypeError("Argument should be a integer")

    if num == 0:
        return (0, 0)

    count_of_even = 0
    count_of_odd = 0

    while num:
        last_digit = int(num % 10)
        if last_digit % 2 == 0:
            count_of_even += 1
        else:
            count_of_odd += 1
        num = num // 10

    return (count_of_even, count_of_odd)

