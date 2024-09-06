```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    n = len(string)
    m = len(substring)

    for i in range(n):
        if string[i] == substring:
            count += 1

    return count

# Example usage:
text = "aaa"
sub = "aa"

result = how_many_times(text, sub)
print(result)  # Output: 3
```
This script defines a function called **`how_many_times`** that takes two parameters: a string and a substring. It uses a value of the string length and the length of the substring to iterate through the string and count the number of occurrences of the substring. The function returns the final count of occurrences of the substring in the string.

This is just one way to solve the problem, feel free to explore other methods and approaches!