```python
def median(l):
    """Return median of elements in the list l.
    if len(l) < 1:
        raise ValueError("List cannot be empty")
    if len(l) % 2 == 0:
        return (l[len(l) // 2 - 1] + l[len(l) // 2]) / 2
    else:
        return l[len(l) // 2]

#Test the function with a list of numbers
numbers = [
    -10, 4, 6, 1000, 10, 20, 30, 40, 50, 60, 70, 80, 90
]
try:
    print(median(numbers))
except ValueError as e:
    print(e)
```