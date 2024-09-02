
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
    # lst1 = list1.join("")
    # lst2 = list2.join("")
    # if len(lst1) < len(lst2):
    #     return list1
    # elif len(lst2) < len(lst1):
    #     return list2
    # else:
    #     return list1
    # return list1

    total_chars1 = sum(len(x) for x in lst1)
    total_chars2 = sum(len(x) for x in lst2)
    if total_chars1 < total_chars2:
        return lst1
    else:
        return lst2

