```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.find(substring) != -end]

# Unit tests
strings = ["abc", "bacd", "cde", "array", "hello"]
substrings = ["a", "ab", "ac", "add", "array"]

test_strings = [
    "This is a test",
    "Everything comes",
    "from England",
    "but nothing stays"
]

test_substrings = [t for t in test_strings if t.find("This")]

print(f"Test case 1: {test_strings[0]}")(test_substrings[0])
print(f"Test case 2: {test_strings[1]}")(test_substrings[1])
print(f"Test case 3: {test_strings[2]}")(test_substrings[0])
print(f"Test case 4: {test_strings[3]}")(test_substrings[2])
print(f"Test case 5: {test_strings[4]}")(test_substrings[1])
print(f"Test case 6: {test_strings[5]}")(test_substrings[0])

print("\nOutput:")
```