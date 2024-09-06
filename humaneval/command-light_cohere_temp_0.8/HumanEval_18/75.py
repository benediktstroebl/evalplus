```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    n = len(string)

    for i in range(n):
        if string[i] == substring:
            count += 1

    return count

# Test cases
string1 = "aaaaaa"
string2 = "a"
substring = "a"

result1 = how_many_times(string1, substring)
print("Result for string1:", result1)

result2 = how_many_times(string2, substring)
print("Result for string2:", result2)
```
The above Python script defines a function `how_many_times` that finds the count of occurrences of a given substring in a given string. The function iterates over the