
def total_match(lst1, lst2):
    '''
    Write a function that accepts two lists of strings and returns the list that has 
    total number of chars in the all strings of the list less than the other list.

    if the two lists have the same number of chars, return the first list.

    Examples
    total_match([], []) ➞ []
    total_match(['hi', 'admin'], ['hI', 'Hi']) ➞ ['hI', 'Hi']
    total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) ➞ ['hi', 'admin']
    total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) ➞ ['hI', 'hi', 'hi']
    total_match(['4'], ['1', '2', '3', '4', '5']) ➞ ['4']
    '''
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # Tried to solve it myself but couldn't. 
    # Had no idea how to proceed. 
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    def sol(lst1, lst2):
        if sum(map(len,lst1))<sum(map(len,lst2)):
            return lst1
        elif sum(map(len,lst2))<sum(map(len,lst1)):
            return lst2
        else:
            return lst1
    return sol(lst1, lst2)
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #




