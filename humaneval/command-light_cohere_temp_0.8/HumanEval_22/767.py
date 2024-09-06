```python
from typing import List

def filter_integers(values:
    """ 
    filtered_ints = [int(item) for item in values if item.isdigit()]
    
    
    if not filtered_ints:
        return []  # Return empty list if no valid integers
    return filtered_ints

# Unit tests
test_filter_integers = []
test_filter_integers.append(['a', 3.14, 5])
test_filter_integers.append([1, 2, 3, 'abc', {}, []])
test_filter_integers.append([1, 2, 3])

# Test cases
test_cases = [test_filter_integers]

result = filter_integers(test_cases)

# Print results
print(result)
```