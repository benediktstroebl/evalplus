Here's a Python function that solves the problem you've described, along with a markdown code block showing the complete script:
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

This script defines a function called `how_many_times` that takes two strings as input: `string` and `substring`. The purpose of this function is to count how many times the `substring` occurs within the `string`, including cases where the `substring` appears multiple times or partially overlaps with itself. 

The function achieves this by initializing a count variable to 0, setting appropriate boundaries using the lengths of the `substring` and `string`, and then looping through the appropriate range of indices. During each iteration, it checks if the substring matches the current slice of the string, and if it does, the count variable is incremented. Finally, the function returns the calculated count.

The test cases are also provided to validate the function's behavior, ensuring that it produces the expected results for various scenarios. You can use these test cases to verify the correctness of the function and ensure that it adheres to the problem statement's requirements.