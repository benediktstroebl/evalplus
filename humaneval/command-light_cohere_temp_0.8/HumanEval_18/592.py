```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count all occurrences of a substring in a string, 
    including overlapping substring matches.
    Returns number of substring occurrences.
    """

def test_function():
    string = "aaaaaaa"
    substring = "aa"
    result = how_many_times(string, substring)
    assert result == 3
    """

This code defines a function called `how_many_times` that calculates and returns the number of occurrences of a given substring within a larger string. The function utilizes a simple string matching and counts all occurrences, including cases with overlapping substring matches. The `test_function` verifies the accuracy of the `how_many_times` function by comparing its result with the expected output for a specific input string and substring combination.