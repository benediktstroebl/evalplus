
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
    total_list = []
    for element in lst1:
        total_chars = 0
        for char in element:
            total_chars += ord(char)
        total_list.append(total_chars)

    total_list2 = []
    for element in lst2:
        total_chars = 0
        for char in element:
            total_chars += ord(char)
        total_list2.append(total_chars)
    
    if len(total_list) > len(total_list2):
        return lst2
    elif len(total_list) < len(total_list2):
        return lst1
    else:
        return lst1
