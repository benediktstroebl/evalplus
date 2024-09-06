```python
def count_distinct_characters(string: str) -> int:
    return len(set(string))

string = "xyzXYZ jerry"
print(count_distinct_characters(string))
```
Do this code first convert the string to lowercase and then create a set of characters. This set contains all characters from the string, which will contain all the distinct characters. We then use the It calculate the length of this set and return the result, which is the number of distinct characters in the string.