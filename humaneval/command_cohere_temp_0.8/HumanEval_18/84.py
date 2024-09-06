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
print(how_many_times('', 'a'))  # Output: 0
print(how_many_times('aaa', 'a'))  # Output: 3
print(how_many_times('aaaa', 'aa'))  # Output: 3
```

This script defines a function `how_many_times` that takes a string `string` and a substring `substring` as input, and counts the number of times the substring occurs in the string, including overlapping instances. It uses a loop to iterate over possible starts of the substring and compares it to the substring of the same length. The script also includes test cases to demonstrate how the function works. You can copy and paste this code into a Python environment or script to test it out.  This solution is feasible and efficient with a time complexity of O(n) where n is the length of the big string.