```python
def median(lst):
    if len(lst) < 1:
        raise ValueError("Input list cannot be empty.")
    elif len(lst) == 1:
        return lst[0]
    else:
        middle = len(lst) // 2
        left_value = lst[middle - 1]
        right_value = lst[middle]
        return (left_value + right_value) / 2

# Example usage:
try:
    median([-10, 4, 6, 1000, 10, 20])
except Exception as e:
    print(f"Error: {e}")
```
Do you need anything else?