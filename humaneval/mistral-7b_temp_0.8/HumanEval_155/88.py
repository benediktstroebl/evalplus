
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    # code here
    counter = 0
    count_even = 0
    for number in str(num):
        if int(number) % 2 == 0:
            count_even += 1
        else:
            counter += 1
    return count_even, counter
