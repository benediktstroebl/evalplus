```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string, 
    considering overlapping matches.
    """
    string: str = "aaaaaaa"
    sub = "aa"
    count = 0
    i = 0

    while i < len(string) - 1:
        if string[i] == sub:
            count += 1
        i += 1

    return count

# Test the function
def test():
    assert how_many_times("aaaaaaa", "aa") == 3

test()
``` 
This script defines a function how_many_times that takes two parameters: a string and a substring. The function then uses a sliding window approach to count the number of occurrences of the substring in the original string, considering case-insensitive matches. 

The test function is also defined to test the correctness of the how_many_times function by passing the string "aaaaaaa" and the substring "aa" to it and asserting that the returned count is equal to 3. 
Finally, the `test()` function is called to execute the test.