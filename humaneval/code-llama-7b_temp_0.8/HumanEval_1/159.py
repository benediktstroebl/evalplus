from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # ------------------------------------------------------------------
    # ANALYSIS PHASE:  Look at the problem and try to think up some
    # ways to solve the problem.  Come up with edge cases and test them.
    # ------------------------------------------------------------------

    # ------------------------------------------------------------------
    # DESIGN PHASE:  Try to figure out the "brute force" way to solve
    # the problem.  Breaking it down into SMALLER sub-problems is often
    # a good strategy.  Look for patterns in the examples.
    # ------------------------------------------------------------------

    def extract_inner_part(paren_string: str) -> str:
        """ Returns a string of everything inside the first set of
        parentheses in the paren_string, including parentheses.
        """
        # --------------------------------------------------------------
        # DRY PHASE:  Do Not Repeat Yourself.  Every time you find
        # yourself copying and pasting some code, think about whether
        # you can reuse what you just wrote instead.
        # --------------------------------------------------------------
        start_index = paren_string.index('(')
        end_index = paren_string.index(')')
        return paren_string[start_index : end_index + 1]

    def remove_outer_part(paren_string: str) -> str:
        """ Returns a string after removing the first set of parentheses
        in the paren_string.
        """
        # --------------------------------------------------------------
        # DRY PHASE:  Do Not Repeat Yourself.  Every time you find
        # yourself copying and pasting some code, think about whether
    # you can reuse what you just wrote instead.
    # ------------------------------------------------------------------
        start_index = paren_string.index('(')
        end_index = paren_string.index(')')
        return paren_string[end_index + 1 :]

    def find_balanced_group(paren_string: str) -> str:
        """ Returns a string of the balanced group in the paren_string,
        including parentheses.
        """
        # -------------------------------------------------
