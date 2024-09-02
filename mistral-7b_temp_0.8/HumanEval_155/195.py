
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    counter = 0
    odd_counter = 0

    for num in str(num):
        if int(num) % 2 == 0:
            counter += 1
        else:
            odd_counter += 1
    return (counter, odd_counter)
