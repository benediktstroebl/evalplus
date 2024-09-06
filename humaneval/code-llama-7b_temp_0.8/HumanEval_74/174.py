
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

    # Create a variable to track the number of chars
    total_chars = 0

    # Get total chars in the first list
    for string in lst1:
        total_chars += len(string)

    # Get total chars in the second list
    for string in lst2:
        total_chars += len(string)

    # Create a variable to track the number of chars in the second list
    total_chars_2 = 0

    # Get total chars in the second list
    for string in lst2:
        total_chars_2 += len(string)

    # Create a variable to track the number of chars in the first list
    total_chars_1 = 0

    # Get total chars in the first list
    for string in lst1:
        total_chars_1 += len(string)

    # If the total chars are equal
    if total_chars == total_chars_1:

        # Return the first list
        return lst1

    # If the total chars are equal
    elif total_chars == total_chars_2:

        # Return the second list
        return lst2

    # If the first list has less chars
    elif total_chars_1 < total_chars_2:

        # Return the first list
        return lst1

    # If the first list has less chars
    elif total_chars_1 > total_chars_2:

        # Return the second list
        return lst2
