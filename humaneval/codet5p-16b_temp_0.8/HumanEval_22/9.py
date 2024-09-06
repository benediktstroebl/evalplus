from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """

    return [value for value in values if isinstance(value, int)]
    # return [value for value in values if isinstance(value, int) and not isinstance(value, bool)]
    # return filter(lambda x: isinstance(x, int), values)
    # return list(filter(lambda x: isinstance(x, int), values))
    # return [x for x in values if isinstance(x, int)]
    # return [x for x in values if not isinstance(x, bool)]
    # return [x for x in values if isinstance(x, int) and not isinstance(x, bool)]
    # return list(filter(lambda x: not isinstance(x, bool), values))

