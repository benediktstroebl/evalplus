
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
    
    total_chars = 0
    final_list = []
    
    for i in range(len(lst1)):
        for c in lst1[i]:
            total_chars += len(c)
        final_list.append(total_chars)
        total_chars = 0
    
    for i in range(len(lst2)):
        for c in lst2[i]:
            total_chars += len(c)
        final_list.append(total_chars)
        total_chars = 0
    
    if final_list[0] <= final_list[1]:
        return lst1
    return lst2
    
    
