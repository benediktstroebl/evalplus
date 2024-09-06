
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
    lst1 = lst1 + lst2
    if len(lst1) > len(lst2):
        lst1, lst2 = lst2, lst1
    lst1_len = len(lst1)
    lst2_len = len(lst2)
    list1 = []
    for element in lst1:
        if len(element) < lst1_len:
            list1.append(element)
    if len(list1) == lst2_len:
        return lst1 
    return list1
    