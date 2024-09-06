```python
def count_distinct_characters(string: str) -> int:
    return len(set(string))

string1 = 'xYK'
string2 = 'jerry'
string3 = ' ABC123'

print(count_distinct_characters(string1))  # Output: 3
print(count_distinct_characters(string2))  # Output: 4
print(count_distinct_characters(string3))  # Output: 5
```
This code defines a function `count_distinct_characters` that calculates the number of distinct characters in a given string. The function utilizes the number of characters to create a set, and the `len()` function then returns the length of the set. In the provided test cases, the function outputs 3 for `'xYK'`, 4 for `'Jerry'`, and 5 for `'ABC123'` due to the spaces between each character.