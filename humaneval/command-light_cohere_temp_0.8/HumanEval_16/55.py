```python
def count_distinct_characters(string: str) -> int:
    return len(set(string))

string = "xyzXYZ jerry aleef"
print(count_distinct_characters(string))  # Output: 6

string = ""
print(count_distinct_characters(string))  # Output: 0

string = "hello"
print(count_distinct_characters(string))  # Output: 4

string = "#!/usr/bin/env python3"
print(count_distinct_characters(string))  # Output: 19
```