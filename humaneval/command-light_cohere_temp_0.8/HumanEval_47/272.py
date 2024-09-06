```python
def median(lst):
    """Return median of elements in the list lst."""
    if len(lst) < 1:
        raise ValueError("Input list is empty.")
    elif len(lst) % 2 == 0:
        return (lst[len(lst) // 2 - 1] + lst[len(lst) // 2]) / 2
    else:
        return lst[len(lst) // 2]

# Test the function with various inputs
for test in [median([-10, 4, 6, 1000, 10, 20]), median([3, 1, 2, 4, 5])]:
    print(test, "->", f(test) ,"rounded to 4 decimal places")
 ```