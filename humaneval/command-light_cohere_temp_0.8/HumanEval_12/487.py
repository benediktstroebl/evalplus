Here's the solution to the markdown code block:
```python
from typing import List

def longest(strings: List[str]) -> List[str]:
    """ Return the length of the longest string.
    """
    length = max(len(string) for string in strings)
    return strings[0] if length == len(strings[0]) else None

# Testing function correctness
test_longest = []
test_longest.add([''.join(), 'abc', 'a'])
test_longest.add(['abc'])
test_longest.add(['abbc'])
test_longest.add(['ab'])
test_longest.add(['ab'])
test_longest.add(['a'])
test_longest.add(['bb'])
test_longest.add(['ccc'])
test_longest.add(['aaa'])
test_longest.add(['acc'])
test_longest.add(['ab'])
test_longest.add(['abcd'])
test_longest.add([ a longest()])
test_result = [len(test_longest[0])]
```