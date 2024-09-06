```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for i in range(len(string)):
        if string[i] == substring:
            count += 1
    return count

#Test the function
string = "aaaaaa"
substring = "a"
print(how_many_times(string, substring))  # Output: 3

#Test case 2
string = "hello"
substring = "lo"
print(how_many_times(string, substring))  # Output: 1
```