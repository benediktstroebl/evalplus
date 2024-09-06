```python
def how_many_times(string, substring):
    return string.count(substring)
```

This function accepts two strings as input: the original string and the substring to search for. It uses the `count()` method to detect the occurrence of the substring within the original string. This method identifies the instance of the substring, whether it is overlapped or not, and returns the count of how many times the substring is found. 

The expected behavior is returned when the substring is absent (`0` times found) or when the substring is repeated several times in the original string. 

This solution has a straightforward implementation and is effective for this problem.  If you want to refine the function's functionality, you can consider encoding the procedure in advance to avoid any potential overlapping matches when the substring occurs more than once in the original string. 

Here are some test cases that can be used to validate the function:
```python
test_cases = [
    ("", "a", 0),
    ("aaa", "a", 3),
    ("aaaa", "aa", 3),
    ("aaa", "aaa", 2),
    ("aaaa", "aaa", 1)
]

for string, substring, expected in test_cases:
    assert how_many_times(string, substring) == expected
```
This test suite contains various test cases to cover different scenarios of the function. Each case takes a `string`, a `substring`, and the `expected` count of occurrences as inputs. The `how_many_times()` function is then called with these inputs, and the actual count of occurrences is compared to the expected count using the `assert` statement. If the actual count matches the expected count, the test passes; otherwise, it fails, alerting us to any unexpected behavior of the function.