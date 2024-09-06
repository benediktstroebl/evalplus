```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    elif len(set(strings)) == 1:
        return strings[0]
    else:
        return max(strings, key=len)
```
This Python script defines a function called longest in the code above that takes a list of strings, called strings, as input, and returns the longest string in the list. If the input list is empty, the function returns None. If there is only one string in the list, the function returns the only string. Otherwise, the function returns the longest string in the list using the max function with the len function as the key. 

Here is an example of how you can test this function:
```python
test_list = ['a', 'bb', 'ccc']
expected_result = 'ccc'

result = longest(test_list)

assert result == expected_result
```
The assert statement will check if the result of the longest function is equal to the expected string, and will pass if they are equal. 

This approach ensures the correctness of the longest function according to the problem statement.