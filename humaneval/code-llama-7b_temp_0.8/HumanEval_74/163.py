
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
    
    lst3 = []
    lst4 = []
    
    if not lst1 and not lst2:
        return lst3
    
    elif lst1 and not lst2:
        return lst1
    
    elif not lst1 and lst2:
        return lst2
    
    else:
        for i in range(len(lst1)):
            for j in range(len(lst2)):
                if sum(len(lst1[i])+len(lst2[j])) == sum(len(lst1[i])+len(lst2[j])) < sum(len(lst1[i])+len(lst2[j])):
                    lst3.append(lst1[i])
                    lst4.append(lst2[j])
    
        if lst3 and lst4:
            return lst3
    
    
