Here's the Python script with a self-contained function `count_distinct_characters` that solves the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
The function `count_distinct_characters` takes a string as an argument and returns the number of distinct characters in the string, regardless of case. It converts each character in the string to lowercase to ensure case insensitivity and then uses a `set` to automatically filter out duplicate characters. It then returns the count of distinct characters.

To apply this function to test cases, the script includes a main entry point that allows you to call the function and print the result for different inputs:
```python
string = 'xyzXYZ'
print(f'Number of distinct characters: {count_distinct_characters(string)}')  # Output: 3

string = 'Jerry'
print(f'Number of distinct characters: {count_distinct_characters(string)}')  # Output: 4
```
This code demonstrates how to solve the problem and handles the given test cases correctly.