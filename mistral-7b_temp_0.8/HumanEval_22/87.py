from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    # We can use `isinstance` to check whether the object is an integer.
    # You can also use `type(obj) == int` to check whether an object is an integer.
    # Or you can use `obj.is_integer` to check whether an object is an integer.
    # But if you use `obj.is_integer` you need to define the `is_integer` method
    # for the class.
    result = []
    for value in values:
        if isinstance(value, int):
            result.append(value)
    return result

