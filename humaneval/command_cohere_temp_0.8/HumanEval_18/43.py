Here's a Python script that contains a function called `how_many_times` which takes a string and a substring as input and returns the number of times the substring occurs within the string, including overlapping occurrences:
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
The function works by iterating through the string starting at every position with a length equal to that of the substring and checks if the substring matches the corresponding part of the string. This algorithm guarantees that all occurrences are counted, including overlapping ones.

Here is an example of how you can use this function:
```python
>>> how_many_times('aaa', 'a')
3
>>> how_many_times('aaaa', 'aa')
3
>>> how_many_times('abc', 'abc')
1
>>> how_many_times('abcabc', 'abc')
2
``` 
This function will handle overlapped instances of the substring and still provide the correct count of occurrences.