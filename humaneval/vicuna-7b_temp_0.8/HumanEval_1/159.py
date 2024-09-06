from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    def count_open_braces(s):
        count = 0
        for char in s:
            if char == '(':
                count += 1
            elif char == ')':
                count -= 1
                if count < 0:
                    raise ValueError(f"Incorrect number of closing parentheses: {count} {len(s)}")
        return count
    
    def extract_pair(s):
        start = s.find('(')
        end = s.rfind(')')
        return s[start:end+1]
    
    left_pairs = []
    right_pairs = []
    for pair in (extract_pair(extract_pair(paren_string))):
        left = count_open_braces(pair)
        right = count_open_braces(pair[1:])
        if left == 0 and right == 0:
            left_pairs.append(pair)
        else:
            right_pairs.append(pair)
    return left_pairs + right_pairs

