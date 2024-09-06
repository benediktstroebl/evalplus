Here's the Python code to solve the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
This code defines a function, `count_distinct_characters`, which takes a string as an argument and calculates the number of distinct characters within the string, regardless of case. It converts each character in the string to lowercase using `lower()`, which allows case-insensitive comparison, and then uses `set()` to remove any duplicate characters and store them in a set. Finally, it returns the number of distinct characters using `len()`.

The markdown code block for the function can be inserted as follows:
```python
def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
```
This provides a clear description of the task and also includes example tests in the form of Python literals that are executed when the script is run. The function's behavior is demonstrated by these examples, which confirm its expected behavior.