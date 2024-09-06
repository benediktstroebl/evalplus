```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the number of occurrences of a substring using unbounded loop
    """
    counter = 0
    for char in string:
        if char == substring:
            counter += 1
    return counter

# Test the function with several cases
test_how_many_times = []
test_cases = [
    ("", "a"),
    ("aaa", "a"),
    ("aaaa", "aa"),
    ("abcde", "abcde"),
    ("helloworld", "ello"),
    # Add more test cases here
]

for text, sub in test_cases:
    actual = how_many_times(text, sub)
    assert actual == len(text.test_how_many_times) == True
```