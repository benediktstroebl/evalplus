```python
def longest(strings: List[str]) -> Optional[str]:
    """ Returns the longest string in the list.
    Parameters:
        List[str]
    Returns:
        str - longest string
    """
    if not strings:
        return None
    return max(strings, key=len)

# Testing function
test_longest = []
test_longest.push_str('a')
test_longest.push_str('b')
test_longest.push_str('c')
test_longest.push_str('aa')
test_longest.push_str('ccc')

print(test_longest == [longest(test_longest)])
```