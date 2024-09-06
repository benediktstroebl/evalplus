```python
def same_chars(s0, s1):
    return len(set(s0) & set(s1)) / min(len(s0), len(s1)) > 0.6
```

The function works by calculating the Jaccard index of the two strings, which is the ratio of the number of characters present in both strings to the minimum of the number of characters in both strings. The threshold of 0.6 is used to determine if two strings have the same characters or not. 

To test this, you can run the following tests:
```python
test_cases = [
    ("eabcdzzzz", "dddzzzzzzzddeddabc", True),
    ("abcd", "dddddddabc", True),
    ("dddddddabc", "abcd", True),
    ("eabcd", "dddddddabc", False),
    ("abcd", "dddddddabce", False),
    ("eabcdzzzz", "dddzzzzzzzddddabc", False)
]

for expected, s0, s1 in test_cases:
    result = same_chars(s0, s1)
    assert result == expected, f"Expected {result} to be {expected}"
```

This code integrates the problem statement, the proposed solution, and the test cases into a complete unit test. 

The function same_chars returns True if the Jaccard index is greater than 0.6, indicating that the two strings have many common characters, and False otherwise. 

The tests check that the function returns the expected result for a variety of test cases.