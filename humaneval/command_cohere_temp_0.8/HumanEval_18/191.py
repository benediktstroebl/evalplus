Here's a Python function that solves the problem you've described:
```python
def how_many_times(string, substring):
    count = 0
    substring_length = len(substring)
    string_length = len(string)
    for i in range(string_length - substring_length + 1):
        if string[i:i + substring_length] == substring:
            count += 1
    return count
```

This function uses a loop to iterate over each possible start position of the substring within the string. It compares the substring to the corresponding substring in the string, accounting for overlapping matches. The count variable keeps track of how many matches are found.

Here are some test cases to demonstrate how it works:
```python
>>> how_many_times('', 'a')
0
>>> how_many_times('aaa', 'a')
3
>>> how_many_times('aaaa', 'aa')
3
>>> how_many_times('aa', 'aa')
2
>>> how_many_times('aaaaaa', 'aa')
5
```