Here's a Python script with a self-contained function that solves the problem you've described, along with a markdown code block:
```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    sub_len = len(substring)
    str_len = len(string)
    for i in range(str_len - sub_len + 1):
        if string[i:i+sub_len] == substring:
            count += 1
    return count

# Test cases
assert how_many_times('', 'a') == 0
assert how_many_times('aaa', 'a') == 3
assert how_many_times('aaaa', 'aa') == 3
```
This script defines a function `how_many_times` that takes a string `string` and a substring `substring` as input and calculates the number of times the substring occurs in the string, including overlapping instances. It then provides three test cases to validate its behavior. 

The function uses a loop to iterate through the string, checking each substring of length equal to the length of the substring being searched for, and increments a count if it matches the substring. The provided test cases demonstrate the correctness of the implementation.  The script is a self-contained code block that solves the specified problem and can be executed independently.  It can be copied and run directly to see the results.