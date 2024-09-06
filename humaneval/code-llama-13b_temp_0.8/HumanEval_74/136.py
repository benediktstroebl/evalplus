
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
    # Easy is obvious.
    # Medium is where I am stuck.
    # Hard is where I am stuck.

    count_one = 0
    count_two = 0
    
    if len(lst1) == len(lst2):
        return lst1
    elif len(lst1) > len(lst2):
        for word in lst2:
            count_two += len(word)
        for word in lst1:
            count_one += len(word)
        if count_one < count_two:
            return lst1
        else:
            return lst2
    else:
        for word in lst1:
            count_one += len(word)
        for word in lst2:
            count_two += len(word)
        if count_one < count_two:
            return lst1
        else:
            return lst2

