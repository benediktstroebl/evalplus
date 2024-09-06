
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
    # if both list are empty return empty list
    if lst1 == [] and lst2 == []:
        return []
    # if first list is empty and second is not return second list
    elif lst1 == [] and lst2 != []:
        return lst2
    # if second list is empty and first is not return first list
    elif lst1 != [] and lst2 == []:
        return lst1
    # if both list are not empty compare them and return the list with less amount of characters
    elif lst1[0] > lst2[0] and lst2 != [] and lst1 != []:
        return lst2
    elif lst1[0] > lst2[0] and lst1 != [] and lst2 == []:
        return lst1
    elif lst1[0] < lst2[0] and lst1 != [] and lst2 != []:
        return lst1
    elif lst1[0] < lst2[0] and lst1 == [] and lst2 != []:
