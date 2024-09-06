
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    # if list is not empty and has length more than 1 
    if len(lst) > 1:
        # set the sum to zero
        sum = 0
        # loop through the list
        for i in range(len(lst)):
            # if index is odd and the value at that index is even
            if (i % 2 != 0) and (lst[i] % 2 == 0):
                # add the value at that index to the sum variable
                sum += lst[i]
        return sum
    # if the list is empty
    else:
        return "List is empty."
