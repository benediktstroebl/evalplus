```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    len_string = len(string)
    for i in range(len_string):
        if string[i] == substring:
            count += 1
    return count

# Test the function
string1 = "aaaaaa"
string2 = "aaa"
substring = "a"
print(how_many_times(string1, substring))  # Output: 3
print(how_many_times(string2, substring))  # Output: 0
 ```