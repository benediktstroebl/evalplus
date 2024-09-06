```python
def flip_case(string: str) -> str:
    return ''.join(char.swapcase() for char in string)
```
This code uses a list comprehension and the `swapcase()` method to quickly and effectively convert each character of the input string to its mirror image in terms of case. This approach ensures that the overall time complexity is O(n), where n is the length of the input string, which is quite efficient for this task.