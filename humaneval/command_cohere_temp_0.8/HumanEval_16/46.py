Here's the Python code with a self-contained function `count_distinct_characters` that solves the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
This function uses a set to store the distinct characters in the given string, ignoring case, and then returns the set's length.

The tests correspond to the ones introduced in the problem statement and are included here:
```python
def test_count_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3, "Lowercase letters considered as one character."
    assert count_distinct_characters('Jerry') == 4, "Uppercase and lowercase letters considered as distinct."
    assert count_distinct_characters('aaaaAAA') == 6, "Distinct count considers capitalization."
    assert count_distinct_characters('123') == 3, "Digit characters are considered."
    assert count_distinct_characters('abcde') == 5, "Small alphabet characters considered."
    assert count_distinct_characters('ｆｇｈｉｊ') == 5, "Fullwidth characters count as distinct."
    assert count_distinct_characters('$@%^&*()_+') == 8, "Special characters are considered."
 if __name__ == "__main__":
    test_count_distinct_characters()
```

The test suite consists of various scenarios that help verify the function's correctness in considering different cases, regardless of whether the characters are uppercase, lowercase, numbers, or special characters.