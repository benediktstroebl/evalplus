```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    len_string = len(string)
    for i in range(len_string):
        if string[i] == substring:
            count += 1
    return count

# Test the function
# Test for different inputs and different lengths of the string and substring.
string = "aaa"
substring = "a"
result = how_many_times(string, substring)
print("Result:", result)

# Test with different lengths
string = "hello"
length = 5
substring = "lo"
result = how_many_times(string, substring)
print("Result:", result)
```