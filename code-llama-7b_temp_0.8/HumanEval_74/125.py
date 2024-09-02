
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

    if len(lst1) == len(lst2):
        return lst1

    lst1_result = 0
    lst2_result = 0

    for i in range(len(lst1)):
        lst1_result += len(lst1[i])

    for i in range(len(lst2)):
        lst2_result += len(lst2[i])
    
    if lst1_result < lst2_result:
        return lst1
    else:
        return lst2
