
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

    # 1. Convert both lists to sets.
    # 2. Find the difference of the two sets.
    # 3. Convert the difference set to a list.
    # 4. Return the difference list.

    # Check that both lists are not empty
    if lst1 and lst2:
        # 1. Convert both lists to sets.
        set1 = set(lst1)
        set2 = set(lst2)

        # 2. Find the difference of the two sets.
        set_diff = set1.difference(set2)

        # 3. Convert the difference set to a list.
        diff_list = list(set_diff)

        # 4. Return the difference list.
        return diff_list
    
    # Return empty list if one or both lists are empty
    else:
        return []
