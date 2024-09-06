```python
def how_many_times(string: str, substring: str) -> int:
    return sum(1 for i, char in enumerate(string) if char == substring)
    
# Test case: Find the number of occurrences of 'a' in the given string.
string = "aaa"
substring = "a"
result = how_many_times(string, substring)
print(f"a" appears {result} times.")
```