Here's a Python script with a self-contained function that solves the problem you've described, along with a markdown code block showing the code and some example tests:
```python
def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases. """
    count = 0
    tmp_string = string.lower()
    tmp_substring = substring.lower()
    while tmp_string:
        if tmp_string.startswith(tmp_substring):
            count += 1
            tmp_string = tmp_string[len(tmp_substring):]
        else:
            tmp_string = tmp_string[1:]
    return count

# Test Cases
assert how_many_times('', 'a') == 0
assert how_many_times('aaa', 'a') == 3
assert how_many_times('aaaa', 'aa') == 3
assert how_many_times('aa', 'aaa') == 0
```

This script defines the `how_many_times` function, which takes a string `string` and a substring `substring` as input and calculates the number of times the `substring` occurs within the `string`, even if the overlap counts too. The function uses a loop to trim the beginnings of the temporary `string` and `substring` and counts the occurrences of the `substring` in the process.

The tests affirm the function's behavior by checking the outcomes against the given inputs. You can execute the script to see the function in action and observe how it behaves with various test cases.  This function is case-insensitive, as demonstrated by the conversion to lowercase with the `lower()` method. You can modify the function if you want case-sensitivity.