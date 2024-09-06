Here's the Python code to solve the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters_set = set(string.lower())
    return len(characters_set)
```
The `count_distinct_characters` function takes a string as input and calculates the number of distinct characters in the string. It converts the input string to lowercase to ensure that uppercase and lowercase variations of each character are considered identical. Then, it utilizes a set to store unique characters only, which naturally removes any duplicate characters, and finally calculates the length of this set to determine the number of distinct characters. The number of distinct characters is returned as the output. 

This solution has a time complexity of O(n) where n is the size of the input string.