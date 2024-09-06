Here's the self-contained Python function to solve the problem:
```python
def count_distinct_characters(string):
    return len(set(string.lower()))

# Example usage:
input_string = 'xyzXYZ'
result = count_distinct_characters(input_string)
print("Distinct characters count:", result)
```

The above function utilizes the `set()` function to create a set of all characters in the input string, and then uses the `len()` function to get the count of distinct characters. The output will be the exact same as the provided initial problem.