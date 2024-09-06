The Python script defines a function **`filter_by_substring`** that filters an input list of strings for a given substring. It utilizes the The filtering approach where the function uses the **`in`** operator and list comprehension to achieve this. The function returns a result is a filtered list of strings that contain the given substring. 

```python
import typing


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring([ 'abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    return [s for s in strings if s.find(substring)]