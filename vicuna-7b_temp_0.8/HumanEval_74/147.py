
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
    # if the two lists have the same number of elements, return the first list
    if len(lst1) == len(lst2):
        return lst1
    # if one list has more elements, return the list with less elements
    if len(lst1) > len(lst2):
        return lst1[:len(lst2)]
    # if the second list has more elements, return the list with less elements
    return lst2[:len(lst1)]
