
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    total = 0
    even_num = 0
    odd_num = 0
    if num < 0:
        num = abs(num)
    while num > 0:
        num = num // 10
        total += 1
    print(total)

    for i in range(total):
        digit = num % 10
        if digit % 2 == 0:
            even_num += 1
        else:
            odd_num += 1
        num = num // 10
    return even_num, odd_num


