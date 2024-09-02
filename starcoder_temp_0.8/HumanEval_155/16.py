
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    # Initialising the count variable
    count = 0

    # if the num is positive
    if num > 0:
        # Iterate over the num
        for i in range(len(str(num))):
            # If the element is odd
            if int(str(num)[i]) % 2 == 1:
                count += 1
            # If the element is even
            else:
                pass
    # If the num is negative
    else:
        # Iterate over the num
        for i in range(len(str(num))):
            # If the element is odd
            if int(str(num)[i]) % 2 == 0:
                count += 1
            # If the element is even
            else:
                pass
    # returning the count
    return (count, len(str(num))-count)

