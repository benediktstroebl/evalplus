```python
def median(lst):
    if len(lst) < 1:
        raise ValueError("Input list must be at least length")
    if len(lst) % 2 == 0:
        return (lst[len(lst) // 2 - 1] + lst[len(lst) // 2]) / 2
    else:
        return lst[len(lst) // 2]

# Example usage:
try:
    print(median([-10, 4, 6, 1000, 10, 20]))
except ValueError as ve:
    print(f"Error: {ve}")
```