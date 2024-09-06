from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    return [s for s in strings if s.startswith(prefix)]


def merge_lists(lst1: List[str], lst2: List[str]) -> List[str]:
    """ Merge two lists, with any duplicates between the two lists removed.
    >>> merge_lists(['a', 'b', 'c', 'd'], ['b', 'c', 'd', 'e', 'f'])
    ['a', 'b', 'c', 'd', 'e', 'f']
    """
    return list(set(lst1 + lst2))


def is_palindrome(s: str) -> bool:
    """ Returns True if the string is a palindrome, that is, the same forwards and
    backwards, and False otherwise.
    >>> is_palindrome('abc')
    False
    >>> is_palindrome('def')
    True
    >>> is_palindrome('ghi')
    False
    """
    return s == rev(s)


def count_chars_in_word(word: str) -> int:
    """ Return the number of characters in a string.
    >>> count_chars_in_word('hello')
    5
    >>> count_chars_in_word('python')
    4
    """
    return len(word)

