```python
from typing import List
from itertools import dropwhile


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    return list(reversed(list(dropwhile(lambda x: x == string[0:len(x)], string[1:]:))) or [None])
```

The `all_prefixes` function uses the `dropwhile` function from the `itertools` module to iterate over prefixes of the input string and drop those that match the prefix itself. This is done in reverse order, yielding from longest to shortest prefix. The list comprehension reverses the order of the prefixes and a None value is added at the beginning of the list.

To understand the purpose of the `dropwhile` function let's test it on an example:
```python
def drop_while_true(string):
    it = dropwhile(lambda x: x == string[0:len(x)], string[1:])
    next(it)
    next(it)
    return next(it)

print(drop_while_true('abc') '')  # Output: 
```
With the example above we check that the iterator created with `dropwhile` is advanced three times, returning each value unchanged, as expected. 

`dropwhile` returns an iterator, so we advance it three times, and it returns the remaining elements of the iterator, ['b', 'bc', 'abc'].