
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
    # sort both lists first
    lst1 = sorted(lst1)
    lst2 = sorted(lst2)

    # get the number of chars in each string of the first list
    num_chars1 = sum([len(word) for word in lst1])

    # get the number of chars in each string of the second list
    num_chars2 = sum([len(word) for word in lst2])

    # compare the two numbers of chars
    if num_chars1 > num_chars2:
        return lst1
    elif num_chars1 < num_chars2:
        return lst2
    else:
        return lst1
