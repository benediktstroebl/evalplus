```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string, taking overlapping cases into account. 
    Args: 
        string: The input string 
        substring: The substring to find in the input string
    """
    return sum(1 for i,x in enumerate(string.find(substring): 1) if x else 0)

# Test
print(how_many_times('aaaa', 'aa')) # 3
print(how_many_times('abcde', 'ab'))  # 2
```