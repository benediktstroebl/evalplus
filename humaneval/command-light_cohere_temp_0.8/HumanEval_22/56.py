```python
from typing import List

def filter_integers(values:
    # filter out the strings and dictionaries
    filtered_values = [value for value in values if isinstance(value, (int, str, dict))]
    return [value for value in filtered_values if value]

# test the function
test_data = [1, 2, 'three', three, [1, 2], {'a': 1, 'b': 2}]
print(filter_integers(test_data))  # expected output: [1, 2, three, 4]
```