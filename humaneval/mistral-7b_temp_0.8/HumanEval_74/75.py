
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
    # append the 1st list to the 2nd
    add_lst = lst2 + lst1
    # append 0 to the 2nd list
    add_lst.append(0)
    # convert each string in the add_lst to a list
    add_lst = [list(str(ele)) for ele in add_lst]
    # find the string with the lowest sum
    min_sum = min([sum(el) for el in add_lst])
    # get the index of the string with the lowest sum
    index = add_lst.index([ele for ele in add_lst if sum(ele) == min_sum])
    # get the string at the index
    return add_lst[index]
