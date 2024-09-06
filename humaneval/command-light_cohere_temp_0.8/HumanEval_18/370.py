Here's a self-contained Python function that solves the problem you described:
```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    length_string = len(string)
    length_substring = len(substring)

    for i in range(1, length_string + 1):
        if string[i - 1] == substring:
            count += 1

    return count
```
This function uses a loop to iterate through every character in the string and checks if the character is equal to the substring. It counts the count the count each time the substring is found. The function is designed to handle overlapping cases by using a counter to count the number of occurrences and return the result.