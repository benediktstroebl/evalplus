from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    # Solution 1:
    # result = []
    # for v in values:
    #     if isinstance(v, int):
    #         result.append(v)
    # return result
    #
    # Solution 2:
    # return list(filter(lambda x: isinstance(x, int), values))

    # Solution 3:
    return [v for v in values if isinstance(v, int)]

