Here's the Python code to solve the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters_set = set(string.lower())
    return len(characters_set)
```
The `count_distinct_characters` function takes a string as an argument and calculates the number of distinct characters in the string. It converts the input string to lowercase to ensure that uppercase and lowercase characters are treated the same. It then utilizes a `set` data structure to remove duplicate characters and retain only unique characters. The length of this `set` is returned as the final result, indicating the count of distinct characters in the string. 

This approach ensures an efficient and accurate way of solving the problem. It's also valuable in highlighting the importance of data structures and the appropriate usage of sets for distinct element counting.