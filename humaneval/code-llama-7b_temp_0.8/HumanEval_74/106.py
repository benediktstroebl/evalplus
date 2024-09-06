
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
    # create a list that will be used to count total number of chars in all strings
    list_of_chars = []

    for i in lst1:
        for j in i:
            list_of_chars.append(j)
    
    for i in lst2:
        for j in i:
            list_of_chars.append(j)

    # count the total number of chars in each string
    len_1 = len(list_of_chars)
    list_of_chars.clear()

    for i in lst1:
        for j in i:
            list_of_chars.append(j)
    
    for i in lst2:
        for j in i:
            list_of_chars.append(j)
    
    len_2 = len(list_of_chars)

    # return the list that has the total number of chars less than the other list
    if len_1 < len_2:
        return lst1
    else:
        return lst2
