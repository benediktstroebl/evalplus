Here is a Python script that includes a self-contained function that solves the problem of finding the number of times a given substring can be found in another string:
```python
import re
def how_many_times(string: str, substring: str) -> int:
    return len(re.findall(substring, string))

# Example usage
text = "aaaaaaa"
substring = "a"
result = how_many_times(text, substring)
print(result)
```

The script uses the re.findall() function from the pattern matching the substring in the text string. The result is the length of the match, which is the count of the number of times the substring appears in the text string.