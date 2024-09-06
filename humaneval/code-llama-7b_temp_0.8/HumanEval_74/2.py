
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

    if len(lst1)==0 or len(lst2)==0:
        return []
    
    total_chars = 0
    for i in lst1:
        total_chars += len(i)
    
    for i in lst2:
        total_chars += len(i)
    
    total_chars1 = 0
    for i in lst1:
        total_chars1 += len(i)

    total_chars2 = 0
    for i in lst2:
        total_chars2 += len(i)

    if total_chars1 == total_chars2:
        return lst1
    elif total_chars1 > total_chars2:
        return lst2
    else:
        return lst1
    
    
