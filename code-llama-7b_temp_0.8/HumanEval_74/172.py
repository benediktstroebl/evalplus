
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
    # Create two variables
    # first_lst = lst1
    # second_lst = lst2

    # Iterate through the first list
    # for first_lst[i] in first_lst:
        # for second_lst[j] in second_lst:
            # add the number of chars to a variable
            # total_chars_first = total_chars_first + len(first_lst[i])
            # total_chars_second = total_chars_second + len(second_lst[j])

    # if total_chars_first < total_chars_second:
        # return first_lst
    # else:
        # return second_lst
    
    

    # if len(first_lst) < len(second_lst):
    #     return first_lst
    # elif len(first_lst) == len(second_lst):
    #     return first_lst
    # else:
    #     return second_lst

    return [lst for lst in (lst1, lst2) if sum(len(word) for word in lst) == sum(len(word) for word in (lst1 if len(lst1) < len(lst2) else lst2))]
