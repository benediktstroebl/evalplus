
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
    # convert both lists to sets
    lst1_set = set(lst1)
    lst2_set = set(lst2)

    # calculate the difference between the two sets
    diff_set = lst2_set.difference(lst1_set)

    # calculate the size of the diff set
    diff_size = len(diff_set)

    # return the first list if it has fewer characters than the other list
    if diff_size < len(lst1):
        return lst1
    else:
        return lst2