```python
from typing import List

def filter_integers(values:
    """ Return integers from a list of various python values.
    return [values contains only integers from a list of any python types.)
    return [num for num in values if isinstance(num, int)]

if __name__ == "__main__":
    values = [3.14, 'a', 5, 1, 2, 'three', [], 0]
    print(filter_integers(values))  # [3, 5, 1, 2]
```