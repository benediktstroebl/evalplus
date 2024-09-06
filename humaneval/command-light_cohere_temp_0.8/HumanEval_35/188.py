```python
def max_element(lst):
    if not_enough_elements(lst):
        return lst[-1]
    else:
        return "Not enough elements"

def not_enough_elements(lst):
    return len(lst) >= 1

# Example usage
result = max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
print("Maximum element:", result)
```