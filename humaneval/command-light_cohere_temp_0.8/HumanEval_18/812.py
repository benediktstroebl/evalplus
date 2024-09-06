```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    string = string.replace(substring)
    while substring in string, count += 1
    return count

# Example usage
text = "aaa"
substring = "a"
print(how_many_times(text, substring))  # Output: 3

```