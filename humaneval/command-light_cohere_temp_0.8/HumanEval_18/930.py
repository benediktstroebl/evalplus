Here is a Python script with a self-contained function that solves the problem you described:
```python
import re
def how_many_times(string: str, substring: str) -> int:
    pattern = re.compile(substring, string)
    return len(pattern.searchall(pattern))
```
Do you require any further assistance with this code?