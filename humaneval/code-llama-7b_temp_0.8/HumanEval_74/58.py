
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
    # pass
    # Your code here
    lst3 = []
    lst4 = []
    for item1 in lst1:
        for item2 in lst2:
            if item1 == item2:
                lst3.append(item1)

    if len(lst3) > len(lst2):
        return lst3
    elif len(lst3) < len(lst2):
        return lst2
    else:
        return lst3


