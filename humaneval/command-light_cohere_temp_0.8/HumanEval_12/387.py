```python
def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    return max(strings, key=len)

# Test the function with a sample input
longest(['a', 'b', 'c'])  # Output: 'c'
longest(['aa', 'bb', 'ccc'])  # Output: 'ccc'
longest([])       # Output: ' '
longest(['a'])     # Will raise ValueError
    ```