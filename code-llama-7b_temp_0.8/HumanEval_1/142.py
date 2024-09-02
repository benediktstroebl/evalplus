from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    def clean_group(group):
        """Cleans up a group by removing all spaces, and then returns a string
        of the resulting group"""
        return group.replace(" ", "")

    def group_to_str(group):
        """Takes a list representing a group and converts it into a string
        representation of that group"""
        return "".join(group)

    def split_group(group):
        """Splits a group up into its constituent parts"""
        output = []
        current_str = ""
        for c in group:
            if c == "(":
                if current_str != "":
                    output.append(current_str)
                    current_str = ""
                current_str += c
            elif c == ")":
                if current_str != "":
                    output.append(current_str)
                    current_str = ""
                current_str += c
            else:
                current_str += c
        output.append(current_str)
        return output

    def clean_groups(groups):
        """Returns a list of cleaned groups, given a list of groups"""
        return [clean_group(group) for group in groups]

    def split_groups(groups):
        """Returns a list of split groups, given a list of cleaned groups"""
        return [split_group(group) for group in groups]

    def flatten_groups(groups):
        """Returns a list of strings, given a list of groups, where each group
        is a list of strings"""
        return [group_to_str(group) for group in groups]

    return flatten_groups(split_groups(clean_groups(separate_paren_groups(paren_string))))

