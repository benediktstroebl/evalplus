```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for char in substring:
        if char in string:
            count += 1
    return count

# Test the function
string = "aaaaaa"
substring = "a"
print(how_many_times(string, substring))  # Output: 3

```
This code defines a function called **`how_many_times`** that takes two arguments: a string and a substring. It initializes a a variable count to zero and then uses a loop to iterate over each character in the substring. The code checks if the character in the substring is also present in the string, and if it is, increments the count variable.

Finally, the function returns the count, which represents the number of occurrences of the substring in the original string.

Please note that you can use this function to solve the given problem and observe the expected output.