
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
    # your code here
    if lst1 == lst2:
        return lst1
    
    lst1_sorted = sorted(lst1)
    lst2_sorted = sorted(lst2)
    
    if lst1_sorted == lst2_sorted:
        return lst1
    
    if len(lst1_sorted) == len(lst2_sorted):
        return lst1_sorted
    
    count = 0
    for a in lst1_sorted:
        if a != lst1_sorted[-1]:
            count += len(a)
    
    for a in lst2_sorted:
        if a != lst2_sorted[-1]:
            count += len(a)
    
    if count < len(lst1_sorted):
        return lst1_sorted
    
    if count < len(lst2_sorted):
        return lst2_sorted
    return []
