```python
def how_many_times(string: str, substring: str) -> int:
    """
    This function counts the occurrences of a given substring within the original string.
    Returns the how substring is passed as an argument, and the function returns the number of occurrences.
    """
    way to find the string and the substring is simple, you can use the string's split method to split the string into individual characters. 

    other cases to check if each character of the substring exists within the original string, you can iterate through each character and check its presence. 
The return value is the number of times the substring was found. 
```

def test_how_many_times():
    """This function runs the function with different inputs and checks if the return values are correct."""
    assert how_many_times("aaa", "aa") == 3
    assert how_many_times("aaaa", "aa") == 3
    assert how_many_times("abcde", "a") == 0
    assert how_many_times("hello world", "o") == 0

```
This code defines a function **`'how_many_times'`** that takes two arguments: a string and a substring. It then returns the read as the number of times the substring appears in the original string, considering case and non-overlapping matches. 

Finally, it defines a test function **`'test_how_many_times'`** that runs the **`'how_many_times'`** function with different inputs and checks if the return values are correct.