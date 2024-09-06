```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string, considering overlapping substring matches.
    """
   
    for match in substring.

    if match in string:
        count += 1
    return count

# Test
string = "aaaabbbcccddd"
substring = "ab"
print(how_many_times(string, substring))  # 3
```