Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    elif len(set(strings)) == 1:
        return strings[0]
    else:
        max_idx = strings.index(max(strings, key=len))
        return strings[max_idx]
```
This script includes the `longest` function that takes a list of strings as input and returns either None, or the longest string from the list, following the specification you provided. The self-contained nature of this script means that it can be copied and run as is, without needing to install additional dependencies. 
The function handles the following cases:
- **Empty list** - Returns None (as per the specification).
- **List with unique strings** - If all strings in the list are of the same length, the function returns the first string (as per the specification).
- **List with multiple strings** - In the case of multiple strings of the same length, the function returns the first one (as per the specification).

The function uses Python's `typing` module to define type annotations for the function parameters and return value. These type annotations can help improve the readability and maintainability of the code, especially when multiple developers are working on a project, and provide better documentation. Here's an example of how you may use this script:
```python
# Import the function from the script
from my_longest_script import longest

# Test the function with different inputs
print(longest([]))  # Expected output: None
print(longest(['a', 'b', 'c']))  # Expected output: 'a'
print(longest(['a', 'bb', 'ccc']))  # Expected output: 'ccc'
``` 
This would output:
```
None
a
ccc
```

It's important to note that this approach uses a simple heuristic to solve the problem and may not be the most efficient for large lists of strings. There are opportunities to optimize the function but those would require additional logic and potentially additional dependencies on libraries beyond the Python standard library. This simplistic approach helps maintain the self-contained trait but may not be the most time-efficient. 

Let me know if you'd like to discuss further optimizations or any other details related to this problem or my approach to it.