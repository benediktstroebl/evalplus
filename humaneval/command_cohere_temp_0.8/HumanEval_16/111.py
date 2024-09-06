Here's the Python code to solve the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
This code defines a function, `count_distinct_characters`, which takes a string as an argument and uses a set data structure to remove duplicate characters, regardless of case. It then returns the length of this modified character set, which represents the number of distinct characters in the string. The tests provided evaluate the function with different inputs and ensure its effectiveness in counting distinct characters. 

Here is an example of how to use this function:
```python
result = count_distinct_characters('xyzXYZ')
print(result)  # Output: 3
```
This demonstrates the function's ability to accurately count the distinct characters in a given string.