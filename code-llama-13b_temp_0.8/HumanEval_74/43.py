
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
    # try to iterate through the first list and sum the number of chars in each string
    first_num_chars = 0
    for string in lst1:
        first_num_chars += len(string)
    
    # try to iterate through the second list and sum the number of chars in each string
    second_num_chars = 0
    for string in lst2:
        second_num_chars += len(string)

    if first_num_chars < second_num_chars:
        return lst1
    elif second_num_chars < first_num_chars:
        return lst2
    else:
        return lst1



