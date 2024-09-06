```python
from typing import List

def filter_integers(values:
    """
    filtered_numbers = [num for num in values if isinstance(num, int)]
    return filtered_numbers

# Test cases
test_values = [['a', 3.14, 5], [1, 2, 'abc', []]
test_results = filter_integers(test_values)

print("Test Cases:", test_values, test_results)

# Filter a list with integers only
input_list = [1, 2, 3, 'abc', [], 5]
filtered_list = filter_integers(input_list)
print("Filtered List:", filtered_list)

```
This script provides a function called `filter_integers` that takes a list of values and returns a new list containing only the integers from the input. The function uses the filter technique to identify the integers in the list and returns the new list. 

Additionally, the script provides test cases to validate the function.