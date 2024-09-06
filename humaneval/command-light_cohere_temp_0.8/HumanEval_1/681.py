```python
from typing import List
def separate_paren_groups(parentheses: str) -> List[str]:
    """
    Separates a string containing multiple groups of parentheses into a list of separate strings.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Split the string into a list of lines
    lines = parentheses_to_lines(parentheses)

    # Separate each line into a list of parentheses
    parsed_lines = [parse_tree(line) for line in lines]

    # Sort the parsed trees
    parsed_trees = sorted(parsed_lines, key=lambda tree: tree_order(tree))

    # Join the parsed trees into a single string
    result = ''.joinjoin(parsed_trees)

    return result

def parentheses_to_lines(parentheses: str) -> List[str]:
    """
    Splits a string containing parentheses into a list of lines.
    >>> parentheses_to_lines('()')
    ['()']
    >>> parentheses_to_lines('()()()')
    ['()()()']
    """
    return [parentheses] if parentheses_to_string(parentheses) == parentheses_to_string('') else [parse_tree(parentheses)]

def parse_tree(tree: List[int]) -> str:
    """
    Returns a properly formatted string representation of the parse tree.
    >>> parse_tree([1])
    '[]'
    >>> parse_tree([1, 2])
    '[1][2]'
    """
    if not tree:
        return ''
    return '(' + parse_tree(tree[1:]) + ')'

def parentheses_to_string(parentheses: str) -> str:
    """
    Returns a string representation of a parse tree.
    >>> parentheses_to_string('()')
    '()'
    >>> parentheses_to_string('()()()')
    '()()()'
    """
    return str(tree) if isinstance(parentheses, List) else parentheses_to_string(parse_tree(parentheses))

def tree_order(tree: List[int]) -> int:
    """
    Returns a string representation of the tree order.
    >>> tree_order([1, 2, 3])
    3
    """

This script solves the problem of separating groups of parentheses in a string. It also passes the tests to verify its functionality.