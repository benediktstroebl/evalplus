
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
    def total_length(lst):
        total = 0
        for i in range(len(lst)):
            total += len(lst[i])
        return total
    
    if len(lst1) == 0 and len(lst2) == 0:
        return []
    if len(lst1) == 0:
        return lst2
    if len(lst2) == 0:
        return lst1

    l1 = total_length(lst1)
    l2 = total_length(lst2)
    if l1 < l2:
        return lst1
    if l2 < l1:
        return lst2
    else:
        return lst1
