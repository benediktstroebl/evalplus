```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for char in string:
        if char == substring:
            count += 1
    return count

# Test the function
string1 = "aaaaaa"
string2 = "aaaa"
string3 = "aaaaaaa"

print("Result of string1:", how_many_times(string1, string1))
print("Result of string2:", how_many_times(string2, string2))
print("Result of string3:", how_many_times(string3, string3))
 ```

This code defines a function called **`how_many_times`** that takes two parameters: a string and a substring. It then uses a string's characters and the substring to count the number of occurrences. The function returns the counting the result.

The function then prints the results of the three strings as an example.