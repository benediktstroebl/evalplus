from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    # ---------------------------------------------------------------------
    # Start by solving the first part of the problem, which is to remove the
    # parentheses.
    # ---------------------------------------------------------------------
    # Split on the parentheses
    words = paren_string.split('(')
    # Remove the closing parentheses
    words = [w.replace(')', '') for w in words]
    # Remove the empty strings
    words = [w for w in words if w]
    # Merge the words
    words = ['(' + w.replace('(', '') for w in words]

    # ---------------------------------------------------------------------
    # Now that we have removed all the parentheses, we have to check the
    # rest of the string to make sure they are balanced.
    # ---------------------------------------------------------------------
    balanced_words = []

    while words:
        first_word = words[0]
        # Remove the first word
        words.pop(0)

        # See if the word is a subset of other words
        is_subset = any([first_word in w for w in words])

        # If the word is a subset of another word, then we have an unbalanced
        # situation.
        if not is_subset:
            balanced_words.append(first_word)
        else:
            # If it is a subset, then it needs to be removed from the list.
            for i, w in enumerate(words):
                if first_word in w:
                    new_word = w.replace(first_word, '')
                    words[i] = new_word

    # ---------------------------------------------------------------------
    # Now we have to reconstruct the parentheses.
    # ---------------------------------------------------------------------
    balanced_words = [w.replace(')', '(') for w in balanced_words]

    return balanced_words

