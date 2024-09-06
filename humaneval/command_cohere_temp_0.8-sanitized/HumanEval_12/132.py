def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.

    :param strings: List of strings to find the longest from.
    :return: Longest string or None if the list is empty.
    """
    # type: <<== declarative semantic alias created from the 'List[str]' type annotation>>
    longest_strings = sorted(strings, key=len, reverse=True)
    return longest_strings[0] if longest_strings else None