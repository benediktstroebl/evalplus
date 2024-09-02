
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if num < 0:
        negative = True
        num = abs(num)
    else:
        negative = False

    list_of_digits = []
    while num > 0:
        list_of_digits.append(num % 10)
        num //= 10

    evens = 0
    odds = 0

    for digit in list_of_digits:
        if digit % 2 == 0:
            evens += 1
        else:
            odds += 1

    if negative == True:
        retun_tuple = (odds, evens)
        retun_tuple = retun_tuple[::-1]
        return retun_tuple
    else:
        return (evens, odds)


