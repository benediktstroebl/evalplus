Here's a Python script that contains a function called `how_many_times` that solves the problem you've described:
```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    substring_length = len(substring)
    string_length = len(string)
    
    for i in range(string_length - substring_length + 1):
        if string[i:i+substring_length] == substring:
            count += 1
    
    return count
```

This function uses a loop to iterate over each possible start position of the substring within the string. It then checks if the substring matches at each position. The loop runs for `string_length - substring_length + 1` to cover all possible positions of the substring within the string or more if you want to allow overlapping counts.

The function is designed to handle empty or blank strings as well.

You can test this function using the Python interpreter as:
```python
>>> how_many_times('', 'a')
0
>>> how_many_times('aaa', 'a')
3
>>> how_many_times('aaaa', 'aa')
3
```

The expected output for these test cases aligns with the problem statement.