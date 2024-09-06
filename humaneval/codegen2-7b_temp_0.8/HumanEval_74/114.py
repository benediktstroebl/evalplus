
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
    lst1.sort()
    lst2.sort()
    i,j = 0,0
    while i<len(lst1) and j<len(lst2):
        if lst1[i] < lst2[j]:
            i+=1
        else:
            j+=1
    while i<len(lst1):
        i+=1
    while j<len(lst2):
        j+=1
    if i == j:
        return lst1
    return lst2
