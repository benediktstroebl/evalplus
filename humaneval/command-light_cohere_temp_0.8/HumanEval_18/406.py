```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    string = ''.join + string
    for _ in range(len(substring)):
        if substring == string[-1:_]:
            count += 1
    return count
#Test case 1
print(how_many_times('', 'a')) # Output: 0
print(how_many_times('aaa', 'a')) # Output: 3
print(how_many_times('aaaa', 'aa')) # Output: 3
```
This script defines a function `how_many_times` that finds the number of occurrences of a given substring within a given string. It uses a general approach by iterating over the substring and checking if the current character is a match to the end of the substring.