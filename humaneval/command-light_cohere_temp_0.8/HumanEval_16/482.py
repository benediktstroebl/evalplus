```python
def count_distinct_characters(string):
    """
    Count the number of distinct characters in a string regardless of case.
    Return: The number of distinct characters.
    """
    unique = set()
    count = 0

    for char in string:
        if char not in unique:
            unique.add(char)
            count += 1

    return count

# Example usage:
string = "xyzXYZ jerry moore"
result = count_distinct_characters(string)
print("Distinct character count:", result)
```