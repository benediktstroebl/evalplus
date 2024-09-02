
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
    # convert strings to sets
    lst1 = [set(word) for word in lst1]
    lst2 = [set(word) for word in lst2]
    # check if the sets have the same number of elements
    if len(lst1) != len(lst2):
        # if the sets have different number of elements, return the list with less number of elements
        return lst1
    else:
        # if the sets have the same number of elements, return the first list
        return lst2
