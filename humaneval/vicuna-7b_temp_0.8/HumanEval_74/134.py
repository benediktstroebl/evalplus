
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
    max_len = max(len(x) for x in lst1 + lst2)
    return [x for x in lst1 if x[:max_len] == x and x != x[max_len+1:]] + [x for x in lst2 if x[:max_len] == x and x != x[max_len+1:]]

lst1 = [1, 2, 3, 4, 5]
lst2 = [1, 2, 3, 4, 5, 6]
result = total_match(lst1, lst2)
print(result)
