from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    def balance(s: str) -> str:
        """ Balance input string by adding open and closing parentheses as needed. """
        opening_parens = re.findall(r'\((.+?)\)', s)
        for opening_paren in opening_parens:
            closing_parens = re.findall(r'\((.+?)\)', opening_paren)
            if len(closing_parens) > 0:
                opening_paren += '({})'.format(',' if closing_parens[0].endswith('(') else ')'
                for closing_paren in closing_parens:
                    opening_paren += '({})'.format(',' if opening_paren.endswith('(') else ')'
        return ''.join(opening_paren for opening_paren in opening_parens)
    def flatten(paren_list: List[str]) -> List[str]:
        """
        Recursively flattens nested groups of parentheses into a single string, while balancing them as needed.
        """
        if not paren_list:
            return []
        flattened_list = []
        for opening_paren in paren_list:
            if '(' in opening_paren:
                opening_paren = balance(opening_paren)
            flattened_list.append(opening_paren)
        for closing_paren in paren_list:
            if ')' in closing_paren:
                closing_paren = balance(closing_paren)
            flattened_list.append(closing_paren)
        return flattened_list
    return flatten(list(map(flatten, [(list(re.findall(r'\((.+?)\)', s)) if s else []) for s in paren_string.split('(')])))

