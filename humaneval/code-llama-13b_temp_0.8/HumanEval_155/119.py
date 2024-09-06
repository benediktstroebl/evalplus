
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    def count_even_odd(num, is_even):
        if is_even:
            return num % 10 % 2 == 0, num // 10
        else:
            return num % 10 % 2 == 1, num // 10

    count = [0, 0]
    while num != 0:
        is_even, num = count_even_odd(num, num > 0)
        count[is_even] += 1
    return tuple(count)

