
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    evens = 0
    odds = 0

    if num < 0:
        num = abs(num)
        num = str(num)
        num = list(num)

        for i in range(len(num)):
            if num[i] % 2 == 0:
                evens += 1
            else:
                odds += 1

        return (evens, odds)
    else:
        num = str(num)
        num = list(num)

        for i in range(len(num)):
            if num[i] % 2 == 0:
                evens += 1
            else:
                odds += 1

        return (evens, odds)
