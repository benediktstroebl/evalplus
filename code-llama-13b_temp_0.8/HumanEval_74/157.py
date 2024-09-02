
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
    # Store the total number of chars in each string of the list
    chars_lst1 = []
    for string in lst1:
        chars_lst1.append(len(string))
    # Store the total number of chars in each string of the list
    chars_lst2 = []
    for string in lst2:
        chars_lst2.append(len(string))
    # Check which list has the total chars less than the other
    if sum(chars_lst1) < sum(chars_lst2):
        return lst1
    elif sum(chars_lst2) < sum(chars_lst1):
        return lst2
    else:
        return lst1

