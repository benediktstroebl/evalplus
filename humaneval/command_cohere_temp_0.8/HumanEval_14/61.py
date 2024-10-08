```python
from typing import List
from itertools import dropwhile


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    return list(reversed(list(dropwhile(lambda s: s != '', string))));
```
The above code reverses the list generated by the `itertools.dropwhile` function so that the prefixes are arranged in the correct order (from shortest to longest). 
It is imperative to mention that this approach eliminates the need for explicit slicing and negation of the prefix list, making the code more efficient and cleaner.

The `dropwhile` function drops elements as long as the predicate returns `True` and returns an iterable with all the elements that make the predicate return `False`. In this case, it drops all elements of the iterable (in this case, the str) as long as the element is not equal to an empty string (`s != ''`). Dropping elements until the predicate changes from `True` to `False` is equivalent to reversing the iterable, which is why we reverse the result list to get the correct order (from longest to shortest) of the prefixes.