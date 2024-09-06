
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

    #check if two lists are empty or not
    if len(lst1) == 0 and len(lst2) == 0:
        return []
    else:
        #useing set to find the length of the two lists
        #If the two lists have the same length, return the first list
        if len(set(lst1)) == len(lst1) and len(set(lst2)) == len(lst2):
            return lst1

        #If the two lists do not have the same length, return the list that has less chars in all strings
        elif len(set(lst1)) != len(lst1) and len(set(lst2)) != len(lst2):
            if len(lst1) < len(lst2):
                return lst1
            else:
                return lst2

        #If the two lists have different lengths, return the list that has less chars in all strings
        elif len(set(lst1)) != len(lst1) and len(set(lst2)) != len(lst2):
            if len(lst1) <
