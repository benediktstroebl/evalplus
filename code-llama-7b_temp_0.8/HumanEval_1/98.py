from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    result = []
    string = paren_string.replace(" ", "")
    if string == "":
        return result
    elif len(string) == 2 and string[0] == "(" and string[1] == ")":
        return [string]
    else:
        paren_stack = []
        string_stack = []
        for index in range(len(string)):
            if string[index] == "(":
                paren_stack.append(string[index])
                string_stack.append([])
            elif string[index] == ")":
                if len(paren_stack) == 0:
                    raise ValueError(
                        "Parentheses are not properly balanced. Some closing braces are missing."
                    )
                elif paren_stack[-1] == "(":
                    string_stack[-1] = "".join(string_stack[-1])
                    paren_stack.pop()
                    result.append(string_stack[-1])
                    string_stack.pop()
                else:
                    raise ValueError("Parentheses are not properly balanced. Some opening braces are missing.")
            else:
                string_stack[-1].append(string[index])
        return result

