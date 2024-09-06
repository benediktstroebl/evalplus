```python
def unique(lst):
    return list(set(lst))

# Test cases
print("Unique function:", unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))  # Output: [0, 2, 3, 5, 9, 123]
print("Unique function with empty list:", unique([]))  # Output: []
print("Unique function with lists:", unique([1, 2, 3, "apple", 4, "banana"]))  # Output: [1, 2, 3, 'apple', 4, 'banana']
print("Unique function with set:", unique({5, 3, 8, 9, 2, 1, 3}))  # Output: [5, 3, 8, 9, 2, 1]
```  This Python script defines a unique function that returns a list containing only the unique elements from the input list. The function is tested with a variety of input lists and sets, and the output is printed to the console.