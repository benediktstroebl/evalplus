```python
def separate_paren_groups(s: str) -> List[str]:
    """
    Separate groups of well-balanced parentheses.

    Args:
        string s: a well-formed string with balanced parentheses.

    Returns: list of strings, each representing a group of balanced parentheses.

    >>> separate_paren_groups('( )((()))())')
    ['(', '(', ')')', ')()']
    """

    def is_balanced(match):
        return len(match) == 4 and match.match(' ) == '()'

    match = re.sub(r'(\)\((\))([)\]', r'\1\2', s)

    groups = [match.split() for match in re.match.split()
    Bib: 'Group' refers to a balanced set of parentheses, such as '()()'.