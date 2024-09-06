Here's the solution along with the markdown code block:
```python
def count_distinct_characters(string):
    return len([c for c in string. operators if c.isalpha()])
 string = 'xyzXYZ'.lower()  # Example string
result = count_distinct_characters(string)
print('<span>'.join(f'Distinct characters: {result}'))
```
This code defines a function `count_distinct_characters` that calculates and returns the count of distinct characters in a given string, regardless of case. This is using a list comprehension with a lambda function to filter out non-alph characters and count them, then converts the example string to lowercase for consistency.