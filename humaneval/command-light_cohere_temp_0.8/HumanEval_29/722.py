```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]


# Test case
test_cases = [
    ['abc', 'bcd', 'cde', 'array'],
    ['haskell', 'c++', 'python'],
    ['data:html', 'link:www'],
    ['a1', 'aa2', 'ab1'],
    ['www. Provide more examples data and. a basic, common practice 

test_by_prefix(['abc', 'bcd', 'cde', 'array'],'a')
    ['cde', 'array']
    ```