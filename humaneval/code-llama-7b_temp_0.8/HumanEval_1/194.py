from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Define the recursive function.
    def recurse(start_index: int, current_output: List[str]) -> List[str]:
        """ This function is recursive. It operates on a string containing a single group of nested parentheses.
        It returns a list of nested groups separated by the outermost parentheses.
        """
        output = []
        # Handle when there is no parentheses.
        if start_index >= len(paren_string):
            output.append(''.join(current_output))
            return output
        # Handle when there is only one parentheses.
        elif paren_string[start_index] == ')' and len(current_output) == 0:
            return ['()']
        # Handle when there is a single parentheses.
        elif paren_string[start_index] == ')':
            return recurse(start_index + 1, [''])
        # Handle when there is no parentheses.
        elif start_index == 0 and paren_string[0] == '(':
            return recurse(1, current_output)
        # Handle when there is an opening parenthesis.
        elif paren_string[start_index] == '(':
            current_output.append(paren_string[start_index])
            return recurse(start_index + 1, current_output)
        # Handle when there is a closing parenthesis.
        elif paren_string[start_index] == ')':
            current_output[-1] += paren_string[start_index]
            return recurse(start_index + 1, current_output)
        else:
            return recurse(start_index + 1, current_output)

    # Call the recursive function.
    return recurse(0, [])

