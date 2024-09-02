from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    list_of_brackets = []
    if paren_string.count(")") == 0:
        list_of_brackets.append(paren_string)
    else:
        for i in range(len(paren_string)):
            if paren_string[i] == "(":
                paren_string = paren_string[i:]
                break
        for j in range(len(paren_string)):
            if paren_string[-j - 1] == ")":
                paren_string = paren_string[:-j - 1]
                break

        num_left_paren = paren_string.count("(")
        num_right_paren = paren_string.count(")")
        if num_left_paren == num_right_paren:
            list_of_brackets.append(paren_string)
            return list_of_brackets
        else:
            while num_left_paren > num_right_paren:
                list_of_brackets.append(paren_string[:paren_string.index(")")])
                paren_string = paren_string[paren_string.index(")") + 1:]
                num_right_paren = paren_string.count(")")
            return list_of_brackets

    return list_of_brackets

