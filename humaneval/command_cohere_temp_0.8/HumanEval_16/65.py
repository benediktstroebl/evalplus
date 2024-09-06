Here's a Python script with a self-contained function that solves the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters_set = set(string.lower())
    return len(characters_set)
```
This function uses a set to count the number of distinct characters in the provided string, regardless of case. It first converts the input string to lowercase to ensure that uppercase and lowercase variations of the same character are counted as one entity and not as distinct characters. Then, it utilizes the `set()` constructor to create a set containing only unique characters from the lowered string. Finally, the `len()` function is applied to the `characters_set` to ascertain and return the quantity of distinct characters present in the original string. 

The function promptly addresses the given problem and furnishes the anticipated outcome, rendering it adaptable and pragmatic for diverse situations necessitating the calculation of distinct characters within a string.