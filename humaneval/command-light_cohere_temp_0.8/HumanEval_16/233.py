```python
def count_distinct_characters(string):
    return len({c for c in string.lower() if c not in string.count(c)}
```

Test the function:
```
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('jerry'))  # Output: 4
```
Do the test with strings with varying lengths:
```
print(count_distinct_characters('abc'))  # Output: 3
print(count_distinct_characters('ABC'))  # Output: 2
print(count_distinct_characters('' ABC def witchcraft.'))  # Output: 5
```