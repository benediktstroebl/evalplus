```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    return [p.format("({%s})", s[::-1].translate(' ', '')) for p, s in zip('(' * s + ')'[::-1], s.translate(' ', ''))]
```
Do you need assistance with anything else?