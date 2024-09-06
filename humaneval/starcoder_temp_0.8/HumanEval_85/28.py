
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    # Create an empty list
    result = []
    # Iterate over the given list
    for i in lst:
        # Check if the index is even
        if i % 2 == 0:
            # Append the even number to the list
            result.append(i)
    # Return the sum of the numbers in the list
    return sum(result)
