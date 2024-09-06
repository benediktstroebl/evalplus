
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
    # try solution
    # 1. Get the length of each string in lst1, store in a list
    # 2. Get the length of each string in lst2, store in a list
    # 3. Find the minimum of the two lists
    # 4. Check if the two lists are equal
    # 4.1 return the first list if they are equal
    # 4.2 return the minimum of the two lists

    lst1_length = []
    lst2_length = []
    if lst1 == [] and lst2 == []:
        return []
    if lst1 != [] and lst2 == []:
        return lst1
    if lst1 == [] and lst2 != []:
        return lst2
    for string in lst1:
        lst1_length.append(len(string))
    for string in lst2:
        lst2_length.append(len(string))
    
    if lst1_length == lst2_length:
        return lst1
    else:
        if sum(lst1_length) < sum(lst2_length):
            return lst1
        elif sum(lst1_length) > sum(lst2_length):
            return lst2

