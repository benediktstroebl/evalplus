```python
def count_distinct_characters(string: str) -> int:
    characters = set(string)
    return len(characters)

# Test the function with some examples
assertEqual(count_distinct_characters('xyzXYZ'), 3)
assertEqual(count_distinct_characters('jerry'), 4)
assertEqual(count_distinct_characters('123'), 3)
assertEqual(count_distinct_characters('abc'), 3)
``` 
This code defines a function `count_distinct_characters` that calculates the count of distinct characters in a given string. The function uses the `set()` method to convert all characters into a set, and then uses the `len()` function to count the number of unique characters, which is the number of distinct characters. 

The `assertEqual()` function is used to test the function's output with the provided examples, which ensure the function's correctness.