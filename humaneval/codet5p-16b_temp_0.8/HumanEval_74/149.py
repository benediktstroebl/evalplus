
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

    total_list = []
    if len(lst1) > len(lst2):
        for i in lst2:
            count = 0
            for char in lst1:
                if len(i) > len(char):
                    if i[0] == char[0]:
                        count += 1
            if count == len(lst1):
                total_list.append(i)
        return total_list
    elif len(lst1) < len(lst2):
        for i in lst1:
            count = 0
            for char in lst2:
                if len(i) > len(char):
                    if i[0] == char[0]:
                        count += 1
            if count == len(lst2):
                total_list.append(i)
        return total_list
    else:
        return lst1

