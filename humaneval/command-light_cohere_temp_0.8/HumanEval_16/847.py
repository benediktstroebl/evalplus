```python
def count_distinct_characters(string):
    return len(set(string.lower()))

x = 'XYZ'
y = 'jerry'

print(count_distinct_characters(x))  # Output: 3
print(count_distinct_characters(y))  # Output: 4
``` 
This function uses the set data structure to count the distinct characters in a given string, regardless of case. It takes advantage of set's 'str.lower()' method to convert all characters to lowercase before taking the set membership test, ensuring that case is ignored.