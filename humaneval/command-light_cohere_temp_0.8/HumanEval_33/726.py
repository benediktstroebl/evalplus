```python
def sort_third(l: list):
    """Sorts a list l of numbers such that all numbers divisible by three are in their correct relative order, and all other numbers are in their original order."""
    # Move numbers divisible by three to the front of the list
    i = 0
    while i < len(l) and l[i] >= 3:
        l[i], l[i+1] = l[i+1], l[i]
        i += 2
    # Move all other numbers to the front of the list
    i = 0
    while i < len(l) and l[i] < 3:
        l[i], l[i+1] = l[i+1], l[i]
        i += 2
    return l
# Test the function
list1 = [5, 6, 3, 4, 8, 9, 2]
print(sort_third(list1))  # Expected Output: [2, 6, 3, 4, 8, 9, 5]
list2 = [10, 20, 30, 40, 50, 12, 22, 18]
print(sort_third(list2))  # Expected Output: [18, 12, 22, 30, 40, 50, 20, 22]
```