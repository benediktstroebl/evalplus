
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

    # We'll use the total chars of each list to compare
    lst1_len = 0
    lst2_len = 0

    # We'll use a for loop to compare the chars of the lists
    for x in lst1:
        lst1_len += len(x)
    
    for x in lst2:
        lst2_len += len(x)
    
    # We check for condition 1
    if lst1_len < lst2_len:
        return lst1
    # We check for condition 2
    elif lst1_len > lst2_len:
        return lst2
    # We check for condition 3
    elif lst1_len == lst2_len:
        return lst1
