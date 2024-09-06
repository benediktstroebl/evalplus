
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
    tot_chars = [0] * len(lst1)
    tot_chars_2 = [0] * len(lst2)
    
    for x in range(0, len(lst1)):
        for y in lst1[x]:
            tot_chars[x] += len(y)
            
    for x in range(0, len(lst2)):
        for y in lst2[x]:
            tot_chars_2[x] += len(y)
    
    if tot_chars > tot_chars_2:
        return lst2
    else:
        return lst1
    
    
