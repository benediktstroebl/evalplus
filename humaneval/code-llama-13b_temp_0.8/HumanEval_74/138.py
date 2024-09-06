
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
    
    t = []
    for i in lst1:
        t.append(sum([len(x) for x in i]))
        
    t2 = []
    for i in lst2:
        t2.append(sum([len(x) for x in i]))
        
    if t[0] > t2[0]:
        return lst2
    elif t2[0] > t[0]:
        return lst1
    elif t2[0] == t[0]:
        return lst1
        
