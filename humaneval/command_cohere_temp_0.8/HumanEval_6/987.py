```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opening, closing in zip(*[iter(s.replace(' ', '').replace(')', ')).split('(') for _ in range(2)])]:
        nest_level = len(list(take_while(lambda c: c=='(', closing))))
        result.append(nest_level)
    return result

def take_while(predicate, sequence):
    """Returns iterator over elements of sequence yielding elements as long as predicate evaluates to True."""
    for element in sequence:
        if not predicate(element):
            break
    return iter(element)
```