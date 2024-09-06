Here's a Python script with a self-contained function that solves the problem you've described, along with a markdown code block showing the code and some example tests:
```python
def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases. """
    count = 0
    idx = 0
    while idx < len(string) - len(substring) + 1:
        found = True
        for i in range(len(substring)):
            if string[idx + i] != substring[i]:
                found = False
                break
        if found:
            count += 1
        idx += 1
    return count

# Tests
assert how_many_times('', 'a') == 0
assert how_many_times('aaa', 'a') == 3
assert how_many_times('aaaa', 'aa') == 3
```
This script defines the `how_many_times` function, which takes a string `string` and a substring `substring` as input and returns the number of times the substring occurs within the string, even if the substring occurs multiple times in individual characters.

The function iterates through the string, checking if the current window of `substring` length is matching from the start to the end. If it matches, it increments the count. This algorithm avoids the complexity of other algorithms like `re` and `str.find()` and works in O(n), where n is the length of the string. 

The tests assert the function's behavior against different cases, ensuring it handles empty strings, matches single characters, and counts overlapping occurrences correctly.