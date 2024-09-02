
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """

    # check list is empty
    if len(lst) == 0:
        return 0
    # if not empty
    else:
        # check if index is even
        if lst[0] % 2 == 0:
            # add item to accumulator
            accum = lst[0]
            # call function again with accumulator and lst[1:]
            accum = accum + add(lst[1:])
            # return accum
            return accum
        # if not even
        else:
            # return lst[0]
            return add(lst[1:])





