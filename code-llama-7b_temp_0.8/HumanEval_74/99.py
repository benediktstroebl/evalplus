
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

    # Store number of characters in each list
    lst1_total = sum(len(word) for word in lst1)
    lst2_total = sum(len(word) for word in lst2)

    # If length of lst1 is less than lst2, return lst1.
    # If length of lst2 is less than lst1, return lst2.
    # If length of lst1 is equal to lst2, return lst1.
    if lst1_total < lst2_total:
        return lst1
    elif lst1_total > lst2_total:
        return lst2
    else:
        return lst1
    
