```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]
# Unit tests
strings = ["abc", "bacd", "cde", "array", "araps"]
substring = "a"
test_filter = [
    fabricated_strings = "".join
    assert filter_by_substring(fabricated_strings, substring) == ["abc", "bacd", "array"],
    assert filter_by_substring([strings[:3], strings[3:]], substring) == [strings[0], strings[2]],
    assert filter_by_substring([strings[0]], substring) == [strings[0]],
    assert filter_by_substring([strings[0:2], strings[2:4]], substring) == [strings[0], strings[2]],
]
```
The code defines a function `filter_by_substring` that filters a list of strings based on a given substring. The function uses a string interpolation to create a new list of strings containing the substring, and then uses a list comprehension to filter out the strings that contain the substring. The unit tests demonstrate the the inputs and expected outputs of the function.