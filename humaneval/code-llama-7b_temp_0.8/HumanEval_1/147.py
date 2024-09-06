from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Separate the input string into a list of strings that are separated by parentheses
    paren_string_list = paren_string.replace(" ", "").split("(")
    # If there are no parentheses, return an empty string
    if paren_string_list == [""]:
        return [""]
    # Remove all the empty strings at the start and end of the list
    paren_string_list = [paren_string_list[0]] + [
        paren_string_list[i] for i in range(1, len(paren_string_list)) if paren_string_list[i] != ""
    ]
    # Initialize a new list to be filled with the separated strings
    separated_strings = []
    # Loop through the list of strings
    for i in range(len(paren_string_list)):
        # If the current string is not empty
        if paren_string_list[i] != "":
            # Remove any spaces in the current string
            paren_string_list[i] = paren_string_list[i].replace(" ", "")
            # If there are more closing parentheses than opening parentheses, add this string to the list
            if paren_string_list[i].count(")") > paren_string_list[i].count("("):
                separated_strings += [paren_string_list[i]]
            else:
                # If there are more opening parentheses than closing parentheses, join all strings until
                # there are an equal number of closing and opening parentheses
                while paren_string_list[i].count("(") > paren_string_list[i].count(")"):
                    # Add the next string to the current one
                    paren_string_list[i] += paren_string_list[i + 1]
                    # Remove the next string from the list
                    paren_string_list[i + 1] = ""
                    # If there are more closing parentheses than opening parentheses, add this string to the list
                    if paren_string_list[i].count(")") > paren_string_list[i].count("("):
                        separated_strings += [paren_string
