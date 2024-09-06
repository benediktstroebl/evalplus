```python
def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string.
    Count overlapping cases
   
    return sum(1 for char in substring in string) 
    """
    return sum(1 for char in substring if char in string) 

def test_how_many_times():
    assert how_many_times('', 'a') == 0
    assert how_many_times('aaa', 'a') == 3
    assert how_many_times('aaaa', 'aa') == 3
    assert how_many_times('aaaaaa', 'aa') == 0
    assert how_many_times('abcde', 'abcd') == 3
    assert how_many_times(' Coleman', 'Col') == 4
```
The code defines a function **`'how_many_times()`** that counts the number of occurrences of a substring within a given string. The function iterates over each character in the substring and the string, and returns **`True`** if the character is a part of the substring, effectively counting its occurrences. The test function verifies the test cases on the function's behavior.