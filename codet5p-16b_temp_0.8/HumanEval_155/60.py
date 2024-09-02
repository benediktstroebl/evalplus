
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

    counter = 0
    count = 0
    num = str(num)
    for n in num:
        if int(n) % 2 == 0:
            counter += 1
            count += 1
        else:
            count += 1
    return (counter, count - counter)
    
