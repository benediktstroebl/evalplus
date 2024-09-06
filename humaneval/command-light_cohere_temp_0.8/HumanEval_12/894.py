```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Returns the longest string in the list.
    """
    # Convert the static type to a mutable list to use the map function
    """
    return max(strings, key=len) if strings else None

# Unit tests
test_longest = []
test_longest.push("a". strings = ['a', 'b', 'c'])
test_longest.push("xy = ['a', 'bb', 'ccc'])
test_longest.push("string_list = ['aa', 'ccc', 'a'])
test_longest.push(None)
test_longest.push("string_list2 = ['a', 'b', 'ccc'])

# Test longest() function with different inputs
result = longest(test_longest.push("string_list2"))
print("Longest string:", result)

# Test result
if result is None:
    print("Error: input list is empty")
elif len(result) == 2:
    print("Error: List has two strings of the same length.")
else:
    print("Correct:", result)

```
This Python script defines a function called `longest` that takes a list of strings as input and returns the length of the longest string in the list. The `test_longest` variable is used to store test cases, which are created by pushing different strings and `None` into the list. The `longest` function is then called with the `test_longest` list and the result is printed.