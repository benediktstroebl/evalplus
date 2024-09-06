from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    def balance_paren(match):
        start, end = match.group(0).index('('), match.group(0).index(')')
        return start, end

    nested = re.findall(r'\((.+?)\)(?=\(.+?\))', paren_string)
    result = []
    for nested_item in nested:
        nested_item = re.findall(r'\([^)]*\)', nested_item)
        nested_item = [nested_item[0].strip()]
        for nested_inner in nested_item:
            nested_inner = re.findall(r'\([^)]*\)', nested_inner)
            nested_inner = [nested_inner[0].strip()]
            nested_item.extend(nested_inner)
        nested_item = ''.join(nested_item)
        result.append(nested_item)
    return result
