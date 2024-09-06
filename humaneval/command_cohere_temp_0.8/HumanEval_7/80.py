```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This code defines a function `filter_by_substring` that takes in a list of strings (`strings`) and a substring (`substring`) as input and returns a new list of strings that contain the specified substring. It uses a list comprehension, iterating over each string in `strings`, and including only those elements that contain the substring `substring`. This is indicated by the inclusion of the `in` operator, which checks for the presence of substring `substring` within string `s`. The resulting list comprehension is accelerated by the use of the `return` statement, which terminates the function return value instantaneously. 
```python
# Sample code for test
strings = ['abc', 'bacd', 'cde', 'array']
substring = 'a'
print(filter_by_substring(strings, substring))
```

The expected output for this test case is:
```
['abc', 'bacd', 'array']
``` 

This demonstrates that the function effectively filters the input list to include only those strings that contain the specified substring. 

This approach has a time complexity of O(n) since it requires iterating through each element in the list once, making it suitable for handling large input lists efficiently.