
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
    
    if lst1 == [] and lst2 == []:
        return []
    elif lst1 == []:
        return lst2
    elif lst2 == []:
        return lst1
    else:
        temp1, temp2 = [], []
        for i in lst1:
            temp1.append(len(i))
        for i in lst2:
            temp2.append(len(i))
        if sum(temp1) < sum(temp2):
            return lst1
        elif sum(temp1) > sum(temp2):
            return lst2
        else:
            return lst1
