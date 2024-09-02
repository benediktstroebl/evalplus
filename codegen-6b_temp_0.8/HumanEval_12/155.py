from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest([])

    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    """
    if not strings:
        return None
    # Use a dictionary to keep track of lengths, only check once.
    # You could also do a set to keep track of the lengths of the words, and then use a list
    # to return the longest one.
    length_of_words = {}
    for word in strings:
        if word not in length_of_words:
            length_of_words[word] = len(word)
        else:
            length_of_words[word] = max(length_of_words[word], len(word))

    max_length = max(length_of_words.values())
    for word in length_of_words:
        if length_of_words[word] == max_length:
            return word
    return None

