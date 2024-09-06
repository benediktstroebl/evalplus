Here's the Python script with a self-contained function `count_distinct_characters` that solves the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
This function uses a set to store the distinct lowercase characters only once, and then calculates the length of this set, which gives the number of distinct characters, regardless of case, in the input string.

To apply this solution directly to your needs, you can use the function like this:
```python
print(count_distinct_characters('xyzXYZ')) # Output: 3
print(count_distinct_characters('Jerry'))  # Output: 4
```
Let me know if this solution suits your requirements, or if you need anything else!