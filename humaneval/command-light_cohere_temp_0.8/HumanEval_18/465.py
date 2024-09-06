```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for i in range(len(string)):
        if string[i] == substring:
            count += 1
    return count

# Test the function
string1 = "aaa"
substring1 = "a"
result1 = how_many_times(string1, substring1)
assert result1 == 3

string2 = "hello"
substring2 = "llow"
result2 = how_many_times(string2, substring2)
assert result2 == 4
```

The above Python script provides a function that finds the frequency of a given substring in a given string. It iterates over the