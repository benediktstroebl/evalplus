
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
    
    #test_1 = []
    #test_2 = []
    
    if len(lst1) == 0:
        return lst1
    elif len(lst2) == 0:
        return lst2
    else:
        n_chars1 = [len(lst1[i]) for i in range(len(lst1))]
        n_chars2 = [len(lst2[i]) for i in range(len(lst2))]
        total_1 = sum(n_chars1)
        total_2 = sum(n_chars2)
    
        if total_1 < total_2:
            return lst1
        elif total_2 < total_1:
            return lst2
        else:
            return lst1
        
