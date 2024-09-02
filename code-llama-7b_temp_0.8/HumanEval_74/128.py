
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
    if not lst1 or not lst2:
        return []
    total_chars_in_list1 = 0
    total_chars_in_list2 = 0

    for string1 in lst1:
        total_chars_in_list1 += len(string1)

    for string2 in lst2:
        total_chars_in_list2 += len(string2)

    if total_chars_in_list1 == total_chars_in_list2:
        return lst1
    elif total_chars_in_list1 < total_chars_in_list2:
        return lst1
    else:
        return lst2
    
