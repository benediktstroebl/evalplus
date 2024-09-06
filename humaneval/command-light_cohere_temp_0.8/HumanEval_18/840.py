Here is a self-contained Python script with a function that finds the number of occurrences of a given substring within a string:
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the occurrences of a given substring in the original string.
    If the unique occurrences in a string of the given substring.
    :string:`substring`
    return number of unique occurrences
    """
    set_of_indices = set(range(string.find(substring)))
    occurrences = len(set_of_indices)
    return occurrences

# Example usage:
def test_how_many_times():
    assert how_many_times('aaa', 'aa') == 3
```
The above Python script defines a function called `how_many_times` that takes two arguments: a string and a substring. The function creates a set of indices where the substring can be found and then returns the count of unique occurrences in that set. The test function `test_how_many_times` is an example of how to use the `how_many_times` function.