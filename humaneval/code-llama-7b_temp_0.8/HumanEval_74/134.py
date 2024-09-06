
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
    sum1 = 0
    for item1 in lst1:
        for letter1 in item1:
            sum1 += len(letter1)
    
    sum2 = 0
    for item2 in lst2:
        for letter2 in item2:
            sum2 += len(letter2)

    if sum1 == sum2:
        return lst1
    elif sum1 > sum2:
        return lst1
    else:
        return lst2
