from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    from unittest import TestCase

    class Test(TestCase):
        def test_separate_paren_groups(self):
            self.assertListEqual(separate_paren_groups('( ) (( )) (( )( ))'), ['()', '(())', '(()())'])
            self.assertListEqual(
                separate_paren_groups('( () ) ((( )))(()()()(()(( ))))'),
                ['(())', '(())', '(()())', '(()(()))', '()((()))'],
            )

    if __name__ == "__main__":
        import doctest

        doctest.testmod()

    return [paren_string.strip(' ') for paren_string in paren_string.strip(' ').split(')(')]

