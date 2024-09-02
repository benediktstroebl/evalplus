from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    def balance(s):
        """ Returns the balanced string s, which is nested parentheses properly closed. """
        return ' '.join(re.findall(r'\(.*?\)(?!\*\* \(.*?\)\*)', s))

    def remove_inner_parentheses(s):
        """ Returns the input string without any inner parentheses. """
        return ' '.join(s.split())

    def flatten_list(lst):
        """ Returns a flat list of elements in a nested list. """
        return flatten(lst)

    def extract_group(s):
        """ Returns the substring of the input string between the open and close parentheses. """
        return s.split('(')[0].split(')')[0]

    def get_next_group(s):
        """ Returns the substring of the input string between the open and close parentheses. """
        i = s.rfind('(')
        if i == -1:
            return s
        j = s.rfind(')')
        if j == -1:
            return s
        return s[i+1:j]

    balanced_string = balance(paren_string)
    flattened_string = remove_inner_parentheses(balanced_string)
    groups = [flatten_list(extract_group(s)) for s in flattened_string.split(' ')]
    return groups
