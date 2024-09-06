```python
def how_many_times(string: str, substring: str) -> int:
    """
    Finds how many times a given substring can be found in the original string, 
    while counting overlapping cases.
    """
    string = 'aaaaaaa'
    sub = 'aa'
    n = 0
    for i in range(len(string)):
        if string[i] == sub:
            n += 1 
    return n
# Test the function
test_string = 'aaaaaaa'
test_substring = 'a'
test_result = how_many_times(test_string, test_substring)
print(test_result)
```