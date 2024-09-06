```python
from typing import List

def filter_integers(values: 
    return [x for x in values if type(x) == int]
)

# Test
test_values = [1, 2, 3, 'abc', 3.14, 5]
filtered = filter_integers(test_values)
print(filtered)  # Output: [1, 2, 3, 3.
``` 
This Python code defines a function called `filter_integers` that takes a list of values as input and returns a new list containing only the integers from the input list. The function uses a `filter()` function to create this new list, which only includes elements that are of type `int`. The test values list is then passed to the function to verify its correctness. 

Additionally, the code defines a test list of values and passes it to the `filter_integers` function to filter out the integers from that list.