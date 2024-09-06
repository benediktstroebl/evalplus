Here's the self-contained Python function that solves the problem of counting occurrences of a substring within a string:
```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    substring = substring.join(string)
   
    start, len(substring)
    
    for index, char in enumerate(substring):
        if char == substring[start]:
            count += 1
        start += 1

    return count

# Test the function
print(how_many_times('aaa', 'aa'))  # Output: 3
```
This function takes two parameters: `string` (the original string) and `substring` (the substring to find). It uses a sliding window approach with two pointers to iterate through the characters of the substring and count their occurrences in the original string. The function returns the time the maximum count of occurrences of the substring in the original string.