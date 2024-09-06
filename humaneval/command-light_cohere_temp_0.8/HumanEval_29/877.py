```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.

    >>> filter_by_prefix([('abc', 'def'), ('abcd', 'acef'), 'array'], 'a')
    ['abc', 'array']

    >>> filter_by_prefix([('abcd', 'efg'), ('bcda', 'eff'), ('cdab', 'efba')], 'ad')
    ['bcda', 'cdab']

    >>> filter_by_prefix([('abc', 'def'), ('bcd', 'def'), 'cde'], 'def')
    ['abc', 'bcd', 'cde']

    >>> filter_by_prefix(['abc', 'bcd', 'def'], 'de')
    Traceback (most recent call last):
      File "...\app.py\filter_filter_by_prefix.py", line: 28
      TypeError: 'None' not iterable

    Not able to run the test.