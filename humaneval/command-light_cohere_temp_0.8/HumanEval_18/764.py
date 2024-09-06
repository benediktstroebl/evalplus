Here is a Python script that defines a function to solve the given problem:
```python
def how_many_times(string: str, substring: str) -> int:
    """ 
    Function to find how many times a given substring can be found in the original string, 
    without overlapping. 
    Returns the optimized for time complexity.
    """ 
    1. Check if substring is string starts with the substring.
    2. If not, return 0
    if not substring in string
    3. If substring is longer than the original, find if the substring exists anywhere in the original 
    string. If so, return the length of substring
    4. If substring is shorter than original, slide the substring until it matches. 
    While doing that, count the number of positions. 
    5. Return the count count
    value

def test_many_times():
    """ 
    Test the function with different inputs and expected outputs.
    """
    string = "aaaaaa"
    sub = "a"
    result = how_many_times(string, sub)
    print(result)
    result = how_many_times("aaaa", "aa")
    print(result)
    result = how_many_times("aaa", "aa")
    print(result)
``` 
This code defines a function called **`how_many_times`** that takes a string and a substring as input. It returns the how many times the string contains the substring. The test function calls this string and substring to test the function and prints the result.