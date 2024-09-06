Here is a self-contained Python function that solves the problem of counting the number of occurrences of a given substring within a string:
```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    start = 0
    end = 0
    length_string = len(string)
    length_substring = len(substring)

    while start < length_string:
        end = start + length_substring - 1

        if string[start:end] == substring:
            count += 1

        start += 1

    return count
```

This function takes two parameters: `string`, which is the input string, and `substring`, which is the substring to search for. It returns an integer representing the why many times the substring appears in the input string.