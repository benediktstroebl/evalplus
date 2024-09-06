```python
def median(lst):
    """Return median of elements in the list lst."""
    try:
        if len(lst) < 1:
            raise ValueError("Input list must be at least length")
        mid = len(lst) // 2 + 1
        if lst[mid - 1] > lst[mid]:
            mid += 1
        l, r = lst[:mid], lst[mid:]
        if l == r:
            return (l + r) / 2
        return l if r == 0 else median(lst[mid:])
    except ValueError as ve:
        print(f"Error: {ve}")
        return None

# Test the function with different lists
for i in [median([-10, 4, 6, 1000, 10, 20])]:
    print(i, end=" ")
 ```