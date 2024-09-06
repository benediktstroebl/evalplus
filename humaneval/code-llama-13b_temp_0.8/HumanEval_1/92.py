from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    # Step 1: Create a list of the index of each open paren
    start_indexes = []
    for index, char in enumerate(paren_string):
        if char == "(":
            start_indexes.append(index)
    # print(start_indexes)

    # Step 2: Create a list of the index of each closed paren
    end_indexes = []
    for index, char in enumerate(paren_string):
        if char == ")":
            end_indexes.append(index)
    # print(end_indexes)

    # Step 3: Pair off the indexes to form ranges
    # Use the current value of i to find a start and end index
    # Use those to calculate the range
    # Use the range to slice the string
    # Convert to a list and add it to a list of strings
    str_list = []
    i = 0
    while i < len(start_indexes):
        start_index = start_indexes[i]
        end_index = end_indexes[i]
        str_list.append(paren_string[start_index : end_index + 1])
        i += 1
    # print(str_list)

    return str_list

