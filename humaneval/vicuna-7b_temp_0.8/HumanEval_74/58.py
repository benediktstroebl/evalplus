
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
    if len(lst1) != len(lst2):
        return lst1
    else:
        return lst2

lst1 = [lst1[i:j] for i in range(len(lst1)) for j in range(len(lst1[i]))]
lst2 = [lst2[i:j] for i in range(len(lst2)) for j in range(len(lst2[i]))]
return total_match(lst1, lst2)
