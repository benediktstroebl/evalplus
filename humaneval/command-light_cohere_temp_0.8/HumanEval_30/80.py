```python
def get_positive(lst):
    """Return only positive numbers in the list"""
    return [num for num in lst if num >= 0]

# Test the function
TestList = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
print("Positive numbers:", get_positive(TestList))

# Test the function with a list of strings
TestList_str = ["hi", "fi", "elveth", "Hello"]
print("Positive numbers from strings:", get_positive(TestList_str))
```