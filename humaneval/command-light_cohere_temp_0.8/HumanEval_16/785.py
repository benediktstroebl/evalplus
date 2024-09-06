```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.string() if c not c.isalpha()} )
   sore counting is:
    set()
    return len(set(string))

x = "XYZ"
y = "yy"
z = "zz"

print(count_distinct_characters(x))  # Output: 3
print(count_distinct_characters(y))  # Output: 4
print(count_distinct_characters(z)))  # Output: 3
```
This code defines a function `count_distinct_characters` that calculates the count of distinct characters in a given string, regardless of case. The distinct characters are identified using a set of characters and the `isalpha()` function checks if a character is an alphabetic value. The `len()` function then counts the number of elements in the set, which is the number of distinct characters in the string.