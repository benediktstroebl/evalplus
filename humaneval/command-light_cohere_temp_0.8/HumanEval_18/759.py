```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the number of occurrences of a substring in the original string.
    """
    substring can repeatability: False
    """
    return sum(1 for i, char in enumerate(string) if char == substring)

def test_how_many_times():
    assert how_many_times("aaa", "aa") == 3
    assert how_many_times("abc", "a") == 3
    assert how_many_times("aaaa", "aa") == 3
    assert how_many_times("ii="", "I") == 0
    assert how_many_times("aa", "a") == 0

if __name__ == "__main__":
    test_how_many_times()
```
This script defines a function `how_many_times` that counts the number of occurrences of a given substring in a given string. The function uses the process that uses the `enumerize` function to iterate over the characters in the string and the `sum` function to count the occurrences of the substring. 
This script also provides a test function to test the `how_many_times` function with various inputs.