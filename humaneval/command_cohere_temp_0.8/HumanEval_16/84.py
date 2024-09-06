Here's the Python code with a self-contained function `count_distinct_characters` that solves the problem:
```python
def count_distinct_characters(s: str) -> int:
    return len(set(s.lower()))
```
This function uses a set to remove duplicate characters and converts the string to lowercase to ensure that cases are not counted separately. It then returns the length of the set, which is the number of distinct characters. The tests correspond to the ones in the Markdown code block. 

```python
test_cases = [
    ("xyzXYZ", 3),
    ("Jerry", 4),
    ("xyzxyzXYZ xyZzYz", 6),
    ("", 0),
    (None, 0),
]

for input, output in test_cases:
    assert count_distinct_characters(input) == output
```