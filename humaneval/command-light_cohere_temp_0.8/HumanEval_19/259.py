```python
from typing import List
def sort_numbers(input_str: str) -> str:
    numbers = input_str.split()
    easy_list: List[int], no_sep='', reverse=False)
    return ' '.join(sorted(easy_list, reverse=reverse), ' ')

def test_sort_numbers():
    return sort_numbers('three one five') == 'one three five'
```