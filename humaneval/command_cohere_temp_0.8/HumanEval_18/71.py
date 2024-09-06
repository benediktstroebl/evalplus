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
The function `how_many_times` takes two strings as input and returns the number of times the `substring` is found within the `string`, including overlapping instances. 
This solution should correctly answer the problem statement for `markdown` code blocks. Let me know if it works as expected!