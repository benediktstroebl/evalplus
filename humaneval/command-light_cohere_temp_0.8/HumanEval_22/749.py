```python
from typing import List
def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test cases
values1 = [1, 2, 3, 'abc', {}, [1, 2, 3]]
values2 = [3.14, 'a', 5]

print("Test case 1: ", end="")
print(filter_integers(values1))
print("\n")

print("Test case 2: ", end="")
print(filter_integers(values2))
``` 
This Python code defines a function called filter_integers that filters out non-integer elements from a given list. The function utilizes the specific typing features in Python and the isinstance function to achieve this. The code then tests this function with two different lists: values1 and values2, and the output is then printed to the console. The output displays the expected results.