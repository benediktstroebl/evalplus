Here's a Python script with a self-contained function that solves the problem you've described, along with a markdown code block showing the complete implementation:
```python
def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases. """
    count = 0
    for i in range(len(string)):
        for j in range(i, len(string)):
            if string[i:j+1] == substring:
                count += 1
    return count

# Test cases
assert how_many_times('', 'a') == 0
assert how_many_times('aaa', 'a') == 3
assert how_many_times('aaaa', 'aa') == 3
```

You can copy and paste this code block into a Python environment or script to test it out. The function `how_many_times` takes a string `string` and a substring `substring` as inputs and returns the number of times the substring occurs within the original string, including overlapping instances. Test cases are also provided to validate the function's behavior.