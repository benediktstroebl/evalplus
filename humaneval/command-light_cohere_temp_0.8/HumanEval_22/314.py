```python
from typing import List

def filter_integers(values:
    return [int(element) for element in values if element.isdigit()]
```
filter_integers(['a', 3.14, 5]) == [5]
filter_integers([1, 2, 3, 'abc', {}, []]) == [1, 2, 3]
filter_integers([123, 25344, 9, "01234"]) == []  # wrong input, should be [123, 25344]
```