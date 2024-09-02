
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if num < 0:
        return (-1, 0)

    if num == 0:
        return (0, 0)

    if str(num) == str(int(num)):
        return (int(num//2), 1)

    count = 1
    for num in str(num):
        if num % 2 == 0:
            count *= 2
        count += 1

    return (count//2, count%2)
