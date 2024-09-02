
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

    list_1 = lst1
    list_2 = lst2
    result = []
    if len(list_1) > len(list_2):
        for i in list_2:
            if i not in result:
                result.append(i)
        return result
    elif len(list_1) < len(list_2):
        for i in list_1:
            if i not in result:
                result.append(i)
        return result
    else:
        for i in list_1:
            if i not in result:
                result.append(i)
        return result
