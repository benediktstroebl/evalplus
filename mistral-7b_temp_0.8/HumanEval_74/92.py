
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
    lst1 = lst1.copy()
    lst2 = lst2.copy()
    while lst1 and lst2:
        #print(lst1)
        #print(lst2)
        if len(lst1[0]) < len(lst2[0]):
            lst1.remove(lst1[0])
        elif len(lst1[0]) == len(lst2[0]):
            lst2.remove(lst2[0])
        else:
            lst2.remove(lst2[0])
    return lst1 + lst2
