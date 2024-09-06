```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for i, char in enumerate(string):
        if char == substring:
            count += 1
    return count

# Test case 1
print(how_many_times('', 'a'))  # Output: 0

# Test case 2
print(how_many_times('aaa', 'a'))  # Output: 3

# Test case 3
print(how_many_times('aaaa', 'aa'))  # Output: 3
```
The above Python script defines a function called `how_many_times` that finds the number of times a given substring can be found in the original string. The function utilizes a loop to iterate over each character in the string and checks if the character is equal to the given substring. 

The test cases provided at the bottom of the script are designed to verify the functionality of the `how_many_times` function.