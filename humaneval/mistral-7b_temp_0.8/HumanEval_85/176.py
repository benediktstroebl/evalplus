
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """

    # The variable i is the index
    i = 0

    # Keep track of the sum using variable sum
    sum = 0

    # Loop through the list lst starting at index 0
    while i < len(lst):

        # If the index is even and the value is even, add to the sum
        if (i % 2 == 0 and lst[i] % 2 == 0):
            sum += lst[i]

        # Increment i
        i += 1

    # Return the sum
    return sum

