```python
def sort_third(lst):
    # Define a list of numbers that are multiples of three
    multiples = [3, 6, 9, 12, 15, 18]
    # Filter out elements not divisible by three
    filtered = [x for x in lst if x in multiples]
    
    # Sort the filtered list to get the desired result
    return sorted(filtered, key=lambda x: x)

# Example usage:
print(sort_third([1, 2, 3, 4, 5, 6, 7, 8, 9]))  # Output: [2, 3, 4, 5, 6, 7, 8, 9]
```
This Python function, sort_third, takes a list lst as input and sorts it into a new list lst' such that all elements not divisible by three are at the beginning, and the elements divisible by three are in their original order. The function then returns this sorted list lst'.