
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if num < 0:
        num = -num

    if num <= 9:
        return (0, 1) if num % 2 else (1, 0)

    num_digits = len(str(num))

    odd_count = 0
    even_count = 0

    num = str(num)

    for i in range(num_digits):
        if int(num[i]) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return even_count, odd_count
