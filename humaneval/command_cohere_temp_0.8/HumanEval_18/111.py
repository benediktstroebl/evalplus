Here's a Python script that contains a function called `how_many_times` which takes a string `string` and a substring `substring` as input and returns the number of times the substring occurs in the string. The function is designed to handle overlapping instances of the substring as well:
```python
def how_many_times(string, substring):
    if not string or not substring:
        return 0
    
    string = string.lower()
    substring = substring.lower()
    
    counter = 0
    n = len(substring)
    
    for i in range(len(string) - n + 1):
        if string[i:i+n] == substring:
            counter += 1
    
    return counter

# Test cases
print(how_many_times('', 'a'))  # Output: 0
print(how_many_times('aaa', 'a'))  # Output: 3
print(how_many_times('aaaa', 'aa'))  # Output: 3
```

This script provides a function that can find and count overlapping instances of a substring within a given string. It does so case-insensitively. The provided test cases ensure the function behaves as expected.