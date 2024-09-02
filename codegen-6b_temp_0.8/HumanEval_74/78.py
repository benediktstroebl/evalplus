
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
    lst1 = sorted(lst1, key=len, reverse=True)
    lst2 = sorted(lst2, key=len, reverse=True)

    if len(lst1) > len(lst2):
        longer = lst1
        shorter = lst2
    else:
        longer = lst2
        shorter = lst1

    for index, char in enumerate(shorter):
        if index < len(shorter) - 1:
            if char == longer[0]:
                shorter = longer[1:]
                longer = longer[1:]
            elif char == longer[1]:
                shorter = longer[1:]
                longer = longer[1:]
            elif char == longer[2]:
                shorter = longer[2:]
                longer = longer[2:]
            elif char == longer[3]:
                shorter = longer[3:]
                longer = longer[3:]
            elif char == longer[4]:
                shorter = longer[4:]
                longer = longer[4:]
            else:
                print(char, longer)
                return longer
    return longer
