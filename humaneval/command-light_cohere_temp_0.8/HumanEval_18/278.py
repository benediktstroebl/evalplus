```python
def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string.
    """
   
    implementation: count occurrences of substring in string
    """
    return len([i for i, char in enumerate(string) if char == substring])

def test_how_many_times():
    assert how_many_times('aaa', 'a') == 3
    assert how_many_times('aaaa', 'aa') == 3
    assert how_many_times('aaaa', 'aaa') == 0
    assert how_many_times('abcde', 'de') == 2
    assert how_many_times('ABCDEFGHIJKLMNOPQRSTUV', 'ABC') == 10
```
This code defines a function `how_many_times` that calculates the number of occurrences of a given substring within a given string. It uses a he `enumerize` function to iterate over every character in the string and count the occurrences of the substring.