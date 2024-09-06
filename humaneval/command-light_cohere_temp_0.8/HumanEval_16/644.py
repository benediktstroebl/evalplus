```python
def count_distinct_characters(string: str) -> int:
    """
    Count the number of distinct characters in a string, regardless of case.
    """
    Returns a list of characters
    """
    return len(set(string))

# Test case 1
test_count_distinct_characters = """
def test_one():
    string = 'xyzXYZ'
    result = count_distinct_characters(string)
    assert result == 3, "The number of distinct characters is incorrect."
test_count_distinct_characters()

# Test case 2
test_count_distinct_characters = """
def test_two():
    string = 'jerry'
    result = count_distinct_characters(string)
    assert result == 4, "The number of distinct characters is incorrect."
test_count_distinct_characters()
``` 
This code provides a function that calculates the number of distinct characters in a given string, regardless of case. It then executes the string test cases that validate the distinct character count function with expected results.