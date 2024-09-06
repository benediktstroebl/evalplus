
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

    # a list of digits in num
    digits = [int(i) for i in str(num)]

    # count even and odd digits
    even_count, odd_count = 0, 0
    for i in digits:
        if i % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return even_count, odd_count

