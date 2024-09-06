```python
def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    max_len = max(len(x) for x in strings)
    return strings[0][:max_len]

def test_longest():
    assert longest(['a', 'b', 'c']) == 'a'
    assert longest(['a', 'bb', 'ccc']) == 'ccc'
```
The provided code defines a Python function `longest` that takes a list of strings as an argument and returns the longest string in the list. The function works by first checking if the input list is empty, in which case it returns `None`. If the list is not empty, it finds the length of the longest string using the `max` function and returns the first character of that string using slicing. 

The code also contains a test function `test_longest` that asserts the correct results of the `longest` function with different input lists.