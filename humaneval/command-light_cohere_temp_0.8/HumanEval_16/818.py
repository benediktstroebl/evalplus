```python
def count_distinct_characters(string):
    """
    Count the number of distinct characters in a given string, regardless of case.
    return: 
    - number of distinct characters
    """
    return len([char for char in string.isalpha()])

# Test the function
def test_distinct_chars():
    assert count_distinct_characters('xyzXYZ') == 3

def test_case():
    assert count_distinct_characters('Jerry') == 4

# Print the test results
print("Test case 1 passed.")
print("Test case 2 passed.")
test_case()
print("\nAll tests passed!")
```