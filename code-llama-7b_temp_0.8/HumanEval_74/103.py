
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
    lst3 = []
    for item in lst1:
        lst3.append(len(item))
    for item in lst2:
        lst3.append(len(item))
    lst4 = []
    for item in lst3:
        lst4.append(item)
    lst4.sort()
    lst4 = lst4[1:]
    lst4.sort(reverse = True)
    for item in lst4:
        if item in lst1:
            lst1.remove(item)
        if item in lst2:
            lst2.remove(item)
    if lst1 == lst2:
        return lst1
    elif lst1 < lst2:
        return lst1
    elif lst2 < lst1:
        return lst2


