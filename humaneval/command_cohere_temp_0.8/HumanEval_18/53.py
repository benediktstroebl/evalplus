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

This function takes two strings as input: the `string` and the `substring`. It returns the number of times the `substring` appears in the `string`, even if there are overlapping occurrences.

To test this function, you can use the following inputs:
```python
>>> how_many_times('', 'a')
0
>>> how_many_times('aaa', 'a')
3
>>> how_many_times('aaaa', 'aa')
3
```

These tests reflect the test cases provided in the original problem and confirm that the function is operating correctly. 

The implementation is straightforward, iterating through the entirety of the larger string and comparing a sliding window of the substring's length to the substring itself. This approach accounts for overlapping instances of the substring as well.