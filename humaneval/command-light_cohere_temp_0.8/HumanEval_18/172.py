```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    n = len(string)
    m = len(substring)

    for i in range(n):
        if string[i:i+m] == substring:
            count += 1

    return count

# Example:
print(how_many_times('aaa', 'a'))  # Output: 3
print(how_many_times('aaaa', 'aa'))  # Output: 3
```
This Python code defines a function called **how_many_times()**, which aims to determine the count of occurrences of a given substring within a given string. The function utilizes a loop to iterate through the original string and compares each substring of length m with the first m characters of the substring. The function counts the necessary occurrences and returns the total count.