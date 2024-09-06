Here's a Python script with a self-contained function that solves the problem you've outlined, including tests:
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
assert how_many_times('aaabbb', 'ab') == 2
```
This script includes a function `how_many_times` that takes a string `string` and a substring `substring` as inputs, and then calculates and returns the number of times the substring occurs within the string. The function iterates through overlapping windows of the input string and checks if each window matches the substring.

The tests were provided as part of the initial prompt, and the code has been updated to include these tests as an integral part of the script. This way, the function's behavior can be validated against these known inputs and expected outputs.