```python
def count_distinct_characters(string):
    return len(set(string.lower()))

x = 'xyzXYZ'
y = 'Jerry'

print(count_distinct_characters(x))  # Output: 3
print(count_distinct_characters(y))  # Output: 4
``` 
The function above calculates the number of distinct characters in a given string, regardless of case. For this, we use the set() function and the `lower()` method to ensure that all characters are converted to lowercase before the set is built, giving all distinct characters while removing duplicates. 

This is a self-contained function with tests that cover the expected behavior of the `count_distinct_characters` function.