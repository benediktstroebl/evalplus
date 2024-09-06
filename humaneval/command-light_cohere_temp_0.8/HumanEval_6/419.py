```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    return [x for x in range(3) for _ in range(len(s) - 2)]  # i.e.c.w.d.t.c.a.a.b.c.d.a.a.d

    dry ( theup the start of the input is the string represented multiple groups for nested parentheses separated by spaces. The function returns a deepest level of nesting of parentheses. 
```

Please feel free to test the function with different input strings!