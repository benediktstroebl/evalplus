
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    oddInd = 1
    evenInd = 0
    while len(lst) > 0:
        if lst[oddInd] % 2 == 0:
            oddInd += 1
            continue
        if lst[evenInd] % 2 != 0:
            evenInd += 1
            continue
        return lst[evenInd]

