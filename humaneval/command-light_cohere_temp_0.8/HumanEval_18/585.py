```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    n = len(string)
    m = len(substring)

    for i in range(n):
        if string[i:i+m] == substring:
            count += 1

    return count

# Test the function
string = "aaaaaa"aa"
substring = "aa"
result = how_many_times(string, substring)
print(result)  # Output: 3
```
This code defines a function how_many_times that takes a string and a substring as input and returns the count of the occurrences of the substring in the original string. The function uses a loop to iterate through the string and checks if a substring of length m is present at position i for n characters. The function keeps track of the count and returns it once the loop completes.