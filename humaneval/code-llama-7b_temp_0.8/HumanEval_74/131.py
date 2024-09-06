
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

    # first check if the two lists are empty, if they are then return an empty list
    if lst1 == [] or lst2 == []:
        return []

    # initialize variables
    total_char_count_1, total_char_count_2 = 0, 0

    # loop through the first list
    for i in lst1:
        # add the length of the current string in the list to the total char count
        total_char_count_1 += len(i)

    # loop through the second list
    for j in lst2:
        # add the length of the current string in the list to the total char count
        total_char_count_2 += len(j)

    # if the total number of chars in the first list is less than the second return the first list
    if total_char_count_1 < total_char_count_2:
        return lst1

    # if the total number of chars in the second list is less than the first return the second list
    elif total_char_count_1 > total_char_count_2:
        return lst2

    # if the two lists have the same number of chars, return the first list
    else:
        return lst1
