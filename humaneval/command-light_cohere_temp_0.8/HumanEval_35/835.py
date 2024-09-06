```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

#Test the function with sample inputs
# Ensure the function returns the correct result
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123

# Test the function with a list of strings
assert max_element(["A", "C", "E"] ) == "E"

# Test the function with a list of custom objects
class SampleObj:
    def __init__(self, x):
        self.x = x
    object.x += 1

def __str__(self):
        return f"{self.x}"
assert max_element([10, 200, 300, 400]) == 300
```