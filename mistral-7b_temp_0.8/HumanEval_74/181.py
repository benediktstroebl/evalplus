
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
    # FILL THE CODE HERE!
    new_list1 = []
    new_list2 = []
    for string in lst1:
        for char in string:
            new_list1.append(char)
    for string in lst2:
        for char in string:
            new_list2.append(char)
    if len(new_list1) > len(new_list2):
        return lst2
    elif len(new_list1) < len(new_list2):
        return lst1
    else:
        return lst1
    print(total_match([], []))
    print(total_match(['hi', 'admin'], ['hI', 'Hi']))
    print(total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']))
    print(total_match(['hi', 'admin'], ['hI', 'hi', 'hi']))
    print(total_match(['4'], ['1', '2', '3', '4', '5']))
    print(total_match(['4', '5'], ['
