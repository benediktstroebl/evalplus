
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
    # Set default to first lst
    least_total = lst1
    # Loop through the first list,
    #   and count the characters in each string
    for i in lst1:
        cnt = len(i)
        # Loop through the second list,
        #   and add the counts together
        for j in lst2:
            cnt += len(j)
        # if the total is lower than the
        #   least_total, set least_total
        #   to the current list
        if cnt < least_total:
            least_total = cnt
            lst_least_total = i
    return lst_least_total
    
    
