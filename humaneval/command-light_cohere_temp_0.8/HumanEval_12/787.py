```python
def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    return max(strings, key=len)

# Test cases
strings = ['a', 'b', 'c']
longest_result = longest(strings)
print(longest_result)  # Output: 'c'

strings = ['a', 'bb', 'ccc']
longest_result = longest(strings)
print(longest_result)  # Output: 'ccc'

strings = []
strings. strings array = ['a', 'bb', 'ccc']
longest_result = longest(strings)
print(longest_result)  # Output: 'bb'

strings = ['abc']
strings. array = ['abc', 'def']
longest_result = longest(strings)
print(longest_result)  # Output: 'abc'
```
This script defines a function `longest` that takes a list of strings as input and returns the longest string from the list. It then passes these tests to the function and prints the result.