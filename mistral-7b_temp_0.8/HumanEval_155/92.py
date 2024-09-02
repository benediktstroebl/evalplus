
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    # code goes here
    count = 0
    for num in str(num):
        if num % 2 == 0:
            count += 1
        else:
            count -= 1
    return count
