from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    return list(filter(lambda x: isinstance(x, int), values))


    'name': 'Filter Integers',
    'author': 'Sindre Sorhus',
    'url': 'http://www.sindresorhus.com',
    'license': 'MIT',
    'original_id': 'ea8e61c1a61d4d609c4450d2844a7827'
