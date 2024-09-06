from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    # [:-1] in the end is to trim the last `,` that was added to make it valid python code
    return f"[concat({', '.join(map(repr, strings))})]"

