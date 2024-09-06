```python
def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    return max(strings, key=len)

# Test the function with various inputs
print(longest(['a', 'b', 'c']))  # Output: 'a'
print(longest(['aa', 'bb', 'ccc']))  # Output: 'ccc'
print(longest([]))  # Output: None
print(longest(['abcde', 'aeifgnop', 'onlyboom']))  # Output: 'abcde'
``` 
The function `longest` takes a list of strings as input and returns the longest string in the list. It returns `None` if the string list is empty.