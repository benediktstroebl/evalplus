Here's a Python script with a self-contained function that solves the problem you've described, along with a markdown code block:
```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    sub_len = len(substring)
    for i in range(len(string) - sub_len + 1):
        if string[i:i+sub_len] == substring:
            count += 1
    return count
```
The function `how_many_times` takes in a string `string` and a substring `substring` as inputs, and returns the number of times the substring occurs in the string, including overlapping occurrences. It uses a for loop to iterate over the length of `string`, and checks each substring of length `substring` for equality with `substring`, incrementing the count accordingly.

The function is tested below via a series of example tests, assert statements that ensure the function behaves as expected:
```python
Test how_many_times():
    assert how_many_times('', 'a') == 0
    assert how_many_times('aaa', 'a') == 3
    assert how_many_times('aaaa', 'aa') == 3
    assert how_many_times('aaa', 'aaa') == 1
    assert how_many_times('aaaaaa', 'aaaa') == 2
    assert how_many_times('abcd', 'ab') == 1
    assert how_many_times('aaaa', 'b') == 0
``` 

This is a basic set of example tests for this function, providing logical inputs and expected outputs.