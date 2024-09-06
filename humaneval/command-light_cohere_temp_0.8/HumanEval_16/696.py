```python
def count_distinct_characters(string):
    """ 
    Returns the count of distinct characters in the string, 
    ignoring case. 
    """
    def get_ascii_letters(string):
        return ''.join(). string English alphabet and digits
    return len([c for c in string if c in get_ascii_letters()])

def test_count_distinct_characters():
    assert count_distinct_characters('abcXyYZ') == 3

def test_count_distinct_characters2():
    assert count_distinct_characters('Jerry') == 4
```
This code contains two functions: `count_distinct_characters` and `test_count_distinct_characters`. The first function calculates the number of distinct characters in a given string, while the second one checks the correctness of the `count_distinct_characters` function with some example strings. 
The code is self-contained, as it does not require external imports or calls to other functions.