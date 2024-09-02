
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
    c1 = sum([len(word) for word in lst1])
    c2 = sum([len(word) for word in lst2])
    if c1 == c2:
        return lst1
    else:
        return lst2

lst1 = [word.lower() for word in lst]
lst2 = map(str.lower, lst2)
lst1 = [sum(1 for char in word if char.isalpha()) for word in lst1]
lst2 = [sum(1 for char in word if char.isalpha()) for word in lst2]
