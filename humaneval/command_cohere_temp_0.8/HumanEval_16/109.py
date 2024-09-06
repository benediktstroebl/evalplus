Here's the Python script with a self-contained function `count_distinct_characters` that solves the problem:
```python
def count_distinct_characters(s: str) -> int:
    return len(set(s.lower()))
```
This function uses a set to filter out all duplicate characters, and then counts the number of distinct characters in the string, regardless of case. The `lower()` method is used to convert all characters in the string to lowercase before counting, thus ensuring that 'Xyz' and 'xyz' are treated as the same character.  An example usage of the function is:
```python
print(count_distinct_characters('xyzXYZ'))  # Outputs: 3
print(count_distinct_characters('Jerry'))  # Outputs: 4
``` 
This approach takes into account the redundancy of characters and gives a consistent method of counting. It is not necessary to change the problem specification or the expected output.