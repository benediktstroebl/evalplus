
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
    lst2_length = len(lst2)
    lst1_length = len(lst1)
    lst1_length_minus_lst2_length = lst1_length - lst2_length
    if lst2_length_minus_lst1_length < 0:
        return lst1
    lst1_minus_lst2 = []
    for index in range(0, lst1_length_minus_lst2_length + 1):
        lst1_minus_lst2.append(lst1[index])
    return lst1_minus_lst2
