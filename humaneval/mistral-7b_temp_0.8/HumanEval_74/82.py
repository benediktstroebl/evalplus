
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
    list_short=[]
    list_long=[]
    #append all the strings into two lists
    for i in lst1:
        list_short.append(i)
    for j in lst2:
        list_long.append(j)
    #find the length of each string
    length_of_short_list = sum(map(len, list_short))
    length_of_long_list = sum(map(len, list_long))
    #compare the total length of the two lists
    if length_of_short_list > length_of_long_list:
        list_short.clear()
        list_short.extend(list_long)
        return list_short
    else:
        list_long.clear()
        list_long.extend(list_short)
        return list_long
