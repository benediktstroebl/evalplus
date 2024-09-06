
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    # TODO: Write your implementation here.
    even, odd = 0, 0
    while num:
        if num & 1:
            odd += 1
        else:
            even += 1
        num >>= 1
    return even, odd
