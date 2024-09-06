```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the number of occurrences of a substring in the original string.
    """
    original_string: str = "Hello World"
    original_substring: str = "dlro"

    count = 0
    start = 0

    while start < len(string):
        if string[start:start+len(original_substring)] == original_substring:
            count += 1
        start += 1

    return count

# Testing the function...
def test_how_many_times():
    assert how_many_times("Hello World", "dlro") == 3
    assert how_many_times("This is a test", "s") == 1
    assert how_many_times("abcde", "de") == 2
    assert how_many_times("Great!", "g") == 2
```
The code defines a function **`how_many_times`** that counts the number of occurrences of a given substring in a given string. The function uses a `start` pointer to search for the substring. 
It moves the pointer forward until it hits the substring and counts the occurrences.