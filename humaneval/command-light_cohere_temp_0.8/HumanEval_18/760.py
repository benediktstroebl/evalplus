```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    length_string = len(string)
    length_substring = len(substring)
    
    for i in range(1, length_string + 1):
        if string[i - 1 : i] == substring:
            count += 1
        
    return count

# Test case # string is 'aaaaaaa' and substring is 'a'
result = how_many_times('aaaaaaa', 'a')
assert result == 3 # Should be 3

# Test case # string is 'aaaa' and substring is 'a'
result = how_many_times('aaaa', 'a')
assert result == 0 # Should be 0

# Test case # string is 'aa' and substring is 'aa'
result = how_many_times('aa', 'aa')
assert result == 2 # Should be 2
```
This script defines a function `how_many_times` that takes two arguments: a string and a substring. The function uses a loop to iterate through the string and counts the number of occurrences of the substring.