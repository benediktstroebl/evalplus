
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
    
    lst = []
    if len(lst1) == len(lst2):
        return lst1
    elif len(lst1) < len(lst2):
        for i in range(len(lst2)):
            x = sum([len(lst1[j]) for j in range(len(lst1))])
            y = sum([len(lst2[j]) for j in range(len(lst2))])
            if x > y:
                lst.append(lst1[i])
            elif x < y:
                lst.append(lst2[i])
            else:
                lst.append(lst1[i])
    else:
        for i in range(len(lst1)):
            x = sum([len(lst1[j]) for j in range(len(lst1))])
            y = sum([len(lst2[j]) for j in range(len(lst2))])
            if x > y:
                lst.append(lst1[i])
            elif x < y:
                lst.append(lst2[i])
            else:
                lst.append(lst1[i])
    return lst
