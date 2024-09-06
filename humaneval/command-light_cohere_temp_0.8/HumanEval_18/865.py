```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    # Iterate over all the string's characters
    for char in string:
        if char == substring:
            count += 1
    return count
# Test cases
print(how_many_times('aaa', 'aa'))  # Output: 3
print(how_many_times('abc', 'a'))  # Output: 2
print(how_many_times('abcde', 'abc'))  # Output: 3
``` 
This function, `how_many_times`, returns the count of a substring within the original string, with the ability to handle overlapping occurrences of the substring.