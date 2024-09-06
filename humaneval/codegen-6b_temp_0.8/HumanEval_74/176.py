
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
    lst1.append(0)
    lst2.append(0)
    for i in range(len(lst1)-1, -1, -1):
        if lst1[i] <= len(lst2[i+1:]):
            lst1[i] = lst1[i] + 1
        if len(lst2) > len(lst1[i+1:]):
            lst2[i] = lst2[i] + 1
    for i in range(len(lst1)):
        if lst1[i] == lst2[i]:
            lst1[i] = lst2[i]
    lst1.pop()
    return lst1

