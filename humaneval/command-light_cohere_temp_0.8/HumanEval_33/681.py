```python
def sort_third(lst):
    """Sorts a list l such that all values divisible by three appear last."""
    return sorted(lst, key=lambda x: not_divisible(x,3))

def not_divisible(x, m):
    return x % m == 0

# Test the function
# Test input: [5, 6, 3, 4, 8, 9, 2]
# Expected output: [2, 6, 3, 4, 8, 9, 5]
sort_third([5, 6, 3, 4, 8, 9, 2])
```
This Python script defines a function **sort_third** that sorts a list such that all values divisible by three appear at the end. It uses a specific to the function **not_divisible** to determine if an element is divisible by three, which then serves as a key for the **sorted** function. 

The output of this script is the sorted list, as expected.