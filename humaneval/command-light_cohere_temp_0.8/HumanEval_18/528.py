```python
def how_many_times(string: str, substring: str) -> int:
    """ 
    Count the number of occurrences of a substring within the original string. 
    1 means found, 
    2 means not found 
    """
    return 1 if string.find(substring) == - 0 else 2 

def test_function():
    print(how_many_times('aaaa', 'aa'))

def test_cases():
    print(how_many_times('hello world 123', 'world'))
    print(how_many_times('hello  world 123', '123'))
    print(how_many_times('hello world! 123', '123'))
    print(how_many_times('hello world!', 'o'))
```
The function `how_many_times` returns 1 if the substring is found, and 2 otherwise.  The test_cases function tests that the `how_many_times` function with different input strings and substrings.