```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return ["".join(char) for char in string]

# Test
test_string = "abc"
test_result = all_prefixes(test_string)
print(test_result)

# Test 2
test_string2 = "hello"
test_result2 = all_prefixes(test_string2)
print(test_result2)
```
This code defines a function `all_prefixes` that returns a list of prefixes from the shortest to the longest characters in the input string. 

In the second part of the code, the function is tested with two different strings.