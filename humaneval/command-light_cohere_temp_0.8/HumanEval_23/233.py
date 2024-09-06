```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)

# Test function to check if strlen works correctly
def test_strlen() -> None:
    assert strlen('') == 0
	assert strlen('abc') == 3
	assert strlen('') == 0 # should return 0, as empty string has no characters
	assert strlen('123') == 3  # should return 3, as '123' has 3 characters

If you find this solution satisfactory, please let me know, and I can assist you further with your Python and coding problems.