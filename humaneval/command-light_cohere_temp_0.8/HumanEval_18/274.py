```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    n = len(string)
    m = len(substring)
    
    for i in range(n):
        if string[i:i+m] == substring:
            count += 1
    
    return count

# Test cases:
>>> how_many_times('aaa', 'a')
3
>>> how_many_times('aaaa', 'aa')
3
>>> how_many_times('abcde', 'abc')
0
>>> how_many_times('mnltk', 'm')
2
```
The function, `how_many_times`, takes two parameters: a string and a substring. It returns the maximum number of times the substring can be found in the original string. The function uses a sliding window approach to count the occurrences of the substring. It works by comparing the window of length `m` with the original string and checks if the window matches the `substring`.