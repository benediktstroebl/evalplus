
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
    
    if len(lst1) == 0 or len(lst2) == 0:
        return []
    
    if len(lst1) == len(lst2):
        return lst1
    
    temp_lst1 = []
    temp_lst2 = []
    
    for i in lst1:
        temp_lst1.append(sum(len(str) for str in i))
        
    for i in lst2:
        temp_lst2.append(sum(len(str) for str in i))
        
    return [lst1, lst2][temp_lst1 > temp_lst2][0]
