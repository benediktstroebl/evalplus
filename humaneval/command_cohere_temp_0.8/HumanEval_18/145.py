Here's a Python script with a self-contained function that solves the problem you've described, along with a markdown code block showing the code and test cases:
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
assert how_many_times('aaabbb', 'ab') == 2
```

The function `how_many_times` takes two strings as input and returns the number of times the substring appears in the original string, even if the overlapping counts are counted multiple times. It iterates through the start positions of the original string, checks for the substring at each position, and increments the count if they match. Test cases are provided to validate the function.  This code block can be copied and pasted into a Markdown file for ease of use.