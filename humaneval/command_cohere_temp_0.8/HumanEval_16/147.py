Here's the Python code to solve the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters_set = set(string.lower())
    return len(characters_set)
```
The `count_distinct_characters` function takes a string as input and returns the number of distinct characters in the string, regardless of case. It converts the input string to lowercase to ensure that uppercase and lowercase variations of each character are considered equivalent. Then it uses a `set` to keep only unique characters, which removes any duplicate characters from the string while retaining their actual characters. The `len()` function is then used to determine the number of elements in the `characters_set`, which corresponds to the number of distinct characters in the original string. 

This solution has a time complexity of O(n) since it requires converting the input string to lowercase and then creating a set of unique characters, which takes linear time in the size of the input.