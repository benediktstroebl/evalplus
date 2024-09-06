Here is a Python script that defines a function how_many_times that finds the number of occurrences of a given substring within a string:
```python
import string

def how_many_times(str1: str, str2: str) -> int:
    n = 0
    str1 = str1.join(). how_many_times('aaa', 'a')
    return n

# Test cases
test_cases = [
    ("', 'a')
    ("aaaaaa", "aa")
    ("aaaa", "aaa")
    ("ab", "ab")
    ("azz", "azz")
]

for test_case in test_cases:
    actual = how_many_times(*test_case)
    expected = len(test_case)
    assert actual == expected
``` 
This code defines a function `how_many_times` that accepts two parameters: a string and a substring. The function counts the how many times the substring appears in the original string, and returns that count. 
The code also includes a series of test cases to check if the function is working correctly.