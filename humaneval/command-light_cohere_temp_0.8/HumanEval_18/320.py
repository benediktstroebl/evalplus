```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for char in substring:
        if char == string[0]:
            count += 1
        string = string[1:]
    return count

# Test cases
test_cases = [
    ("", "a"),
    ("aaa", "a"),
    ("aaaa", "aa"),
    ("abcde", "abcde"),
    ("helloworld", "hello"),
    (" puncture", "puncture"),
    ("🧪", "oxy")
]

for test_case in test_cases:
    actual = how_many_times(*test_case)
    expected = len(test_case)
    assert actual == expected, f"Test case '{test_case}' failed with actual: {actual} and expected: {expected}"
 ```  This code defines a function called **how_many_times**, which returns the number of times a given substring can be found in a given string. It uses a test-style of iteration to find all substrings in the input string and counts the occurrences.