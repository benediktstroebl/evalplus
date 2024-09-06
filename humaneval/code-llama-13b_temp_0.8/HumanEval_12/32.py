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
    longest_string = None
    longest_len = 0
    for string in strings:
        if len(string) > longest_len:
            longest_string = string
            longest_len = len(string)
    return longest_string


    'name': 'Longest',
    'question': 'Which of these is the longest string?',
    'description': 'Write a function that, given a list of strings, returns the longest one',
    'examples': [
        {
            'input': '["a", "bb", "ccc"]',
            'output': '"ccc"'
        }
    ],
    'source_url': 'https://gist.github.com/C-Pound/5581873'
