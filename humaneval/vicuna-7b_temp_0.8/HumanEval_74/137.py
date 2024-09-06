
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
    if len(lst1) == len(lst2):
        return lst1
    else:
        return lst2

lst1 = ['hi', 'admin']
lst2 = ['hI', 'Hi']
result = total_match(lst1, lst2)
print(result)

lst1 = ['hi', 'admin', 'project']
lst2 = ['hI', 'hi', 'hi']
result = total_match(lst1, lst2)
print(result)

lst1 = ['4']
lst2 = ['1', '2', '3', '4', '5']
result = total_match(lst1, lst2)
print(result)