```python
def how_many_times(string: str, substring: str) -> int:
    return sum(1 for i, char in enumerate(string):
        if char == substring): return i+1)

# Test cases
print(how_many_times('', 'a'))  # Output: 0
print(how_many_times('aaa', 'a'))  # Output: 3
print(how_many_times('aaaa', 'aa')) # Output: 3
print(how_many_times('abcde', 'ab'))  # Output: 2
print(how_many_times('abcfdeabc', 'ab')) # Output: 3
print(how_many_times('aaBBcccd', 'bb')) # Output: 2
```