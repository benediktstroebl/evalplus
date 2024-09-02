from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # This is a nice little challenge. I don't know if there's an easy way to solve this, so I went with a
    # naive solution that works in O(n^2) time (n being the length of the paren_string).
    #
    # I iterated over the string, looking for the opening and closing parentheses. Whenever I found an opening
    # parenthesis, I recorded the index of it and its matching closing parenthesis. Whenever I found a closing
    # parenthesis, I checked whether there were any recorded opening parentheses before it. If there were,
    # I checked whether they'd been matched. If they hadn't, I moved the recorded index of the opening parentheses
    # to the end of the string.
    #
    # Now that I've done that, I just iterate over the recorded indices and use the slice notation to grab the
    # substrings of the string.
    opening_indices = []
    closing_indices = []

    for i, char in enumerate(paren_string):
        if char == '(':
            opening_indices.append(i)
        elif char == ')':
            if len(closing_indices) >= len(opening_indices):
                opening_indices.append(len(paren_string))
            else:
                closing_indices[-1] = i
        else:
            continue

    return [paren_string[start:end + 1] for start, end in zip(opening_indices, closing_indices)]

