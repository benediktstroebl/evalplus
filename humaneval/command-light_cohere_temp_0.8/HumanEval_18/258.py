```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    # Iterate over all positions and characters in the string
    for i, c in enumerate(string):
        if c == substring:
            count += 1
    return count

# Test the function with some examples
print(how_many_times('aaa', 'a'))  # Output: 3
print(how_many_times('aaaa', 'aa'))  # Output: 3
print(how_many_times('abcde', 'abc'))  # Output: 2
print(how_many_times('hello world', 'o'))  # Output: 0
```