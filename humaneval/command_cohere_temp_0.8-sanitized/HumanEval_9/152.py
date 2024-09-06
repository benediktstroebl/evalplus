from typing import List, Tuple
def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    return [max(list(window)) for window in zip_longest(numbers, numbers[1:]+[None], fillvalue=None)] \
        [:rolling_window]
def zip_longest(*args, fillvalue=None):
    """Repeat elements in *args* until the longest iterable is exhausted.
    Iterate through the result with the same iteration behavior as itertools.zip_longest.
    Examples
    --------
    >>> list(zip_longest('abc', ['a', 'b']))
    ['a', 'b', 'c']
    >>> list(zip_longest('abc', ['a', 'b', 'c']))
    ['a', 'b', 'c']
    >>> list(zip_longest('abc', ['a', 'b', 'c'], fillvalue='N'))
    ['a', 'b', 'c']
    >>> list(zip_longest( ('abc',), ['a', 'b', 'c'], fillvalue=('N', 0)))
    [('a',), ('b',), ('c',)]
    """
    fillers = [fillvalue]*(max(map(len, args)) - sum(map(len, args)) + 1)
    return itertools.zip_longest(*args, fillvalue=fillers)