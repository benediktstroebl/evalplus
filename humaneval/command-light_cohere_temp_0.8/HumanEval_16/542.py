```python
def count_distinct_characters(string):
    return len(set(string.lower()))

x = 'xyXYZ'
y = 'Jerry'

print(count_distinct_characters(x))  # Output: 3
print(count_distinct_characters(y))  # Output: 4
``` 
This Python function named `count_distinct_characters` accepts a string `string` as input and calculates the count of distinct characters in that string, regardless of case. The function utilizes the uniqueness of characters and stores them in a set, which then calculates the length of that set, giving the count of distinct characters. The function then returns the unique characters in the string.