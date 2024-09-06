
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    # base case
    if num == 0:
        return (0, 0)

    # recurse for even and odd digits separately
    even_count = 0
    odd_count = 0
    for i in range(len(str(num))):
        # if the current digit is even, increment the even count
        if num % 2 == 0:
            even_count += 1
        # if the current digit is odd, increment the odd count
        elif num % 2 == 1:
            odd_count += 1

    return (even_count, odd_count)
