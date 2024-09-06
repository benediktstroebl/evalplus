```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for i, char in enumerate(string):
        if char == substring:
            count += 1
    return count

# Test the function
string1 = "aaa"
substring1 = "a"
result = how_many_times(string1, substring1)
print(result) # prints 3

string2 = "Hello"
substring2 = "ello"
result = how_many_times(string2, substring2)
print(result) # prints 2
```