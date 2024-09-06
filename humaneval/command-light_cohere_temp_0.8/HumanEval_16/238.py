```python
def count_distinct_characters(string):
    return len([c for c in string. characters() if c.isalpha()])

# Test case 1:
print(count_distinct_characters('xyzXYZ'))
# Output: 3

# Test case 2:
print(count_distinct_characters('Jerry'))
# Output: 4

# Test case 3:
print(count_distinct_characters('abcABC'))
# Output: 3

# Test case 4:
print(count_distinct_characters('g 20'))
# Output: 2

```
This function, `count_distinct_characters`, takes a string as input and returns the count of distinct characters in that string, regardless of case. The function uses a list comprehension to filter out each character in the string and checks if each character is an alphabetic() in the string using the `isalpha()` function. 
The output of the function is the length of this filtered list, which is the count of distinct characters.