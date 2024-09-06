Here's a Python script with a self-contained function that solves the problem you've described, along with a markdown code block:
```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    substring_length = len(substring)
    string_length = len(string)
    for i in range(string_length - substring_length + 1):
        if string[i:i+substring_length] == substring:
            count += 1
    return count

# Test cases
assertEqual(how_many_times('', 'a'), 0)
assertEqual(how_many_times('aaa', 'a'), 3)
assertEqual(how_many_times('aaaa', 'aa'), 3)
```

This script defines a function `how_many_times` that takes a string `string` and a substring `substring` as input and calculates the number of times the substring occurs in the string, including overlapping instances. It then includes test cases to ensure the function behaves as expected. You can easily run this code to test the function.  Please replace the `assertEqual` line with the test framework you are using to test the function.