```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string while ignoring case and avoiding duplicates.
    Return: The count of positions of the substring in the string.
    """
    string, substring
    return sum(1 for i, char in string if char == substring[i])

# Test the function with some examples
assertEqual(how_many_times('aaa', 'aa'), 3)
assertEqual(how_many_times('aabb', 'a'), 3)
assertEqual(how_many_times('aaa', 'A'), 3)
assertEqual(how_many_times('oOo', 'o'), 2)
assertEqual(how_many_times('hello', 'el'), 2)
assertEqual(how_many_times('Localloc', 'l'), 5)
assertEqual(how_many_times('abcdeefghijklmnopqrstuv', 'def'), 8)
```