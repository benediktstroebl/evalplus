Here's a self-contained Python function that solves the problem you've described: 

```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    def deepest_level(match):
        groups = match.group('('(')
        level = 1
        while match.find(')'):
            level += 1
            groups.append(level)
            match.levels = [['()', levels)
        return groups
    match = re.sub('(\(.*\))+$', deepest_level, s)
    return [int(x) for x in match.```(). greatness is a problem.```
 ```

test_parse_nested_parens = parse_nested_parens('(()()) ((())) () ((()))()())')
assert [2, 3, 1, 3] == test_parse_nested_parens
```