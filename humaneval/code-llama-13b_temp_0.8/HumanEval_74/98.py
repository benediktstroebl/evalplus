
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
    
    def sum_chars(lst):
        count = 0
        for s in lst:
            count += len(s)
        return count
    
    sum_lst1 = sum_chars(lst1)
    sum_lst2 = sum_chars(lst2)
    
    if sum_lst1 < sum_lst2:
        return lst1
    elif sum_lst2 < sum_lst1:
        return lst2
    else:
        return lst1

