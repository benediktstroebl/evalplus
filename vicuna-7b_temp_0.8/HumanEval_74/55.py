
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
    count1 = 0
    count2 = 0
    i = 0
    while i < len(lst1):
        if lst1[i] == lst2[i]:
            count1 += 1
            i += 1
        else:
            count2 += 1
            i += 1
    return [x for x in lst1 if x not in lst2]

lst1 = ['hi', 'admin', 'hi', 'hi']
lst2 = ['hI', 'Hi', 'hi', 'admin', 'project']
