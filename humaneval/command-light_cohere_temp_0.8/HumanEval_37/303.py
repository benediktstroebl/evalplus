```python
def sort_even(l: list):
    return l[:] if len(l)%2 else l[:] + [l[-1]]

# Test the function
test_even = [5, 6, 3, 4]
test_even_sorted = sort_even(test_even)
print(test_even_sorted)
```
The script defines a function sort_even that takes a list l and returns a new list l_sorted. The function uses an if statement to determine whether the length of the list is even or odd. It returns the list if the list is even, which includes the original list with the last element added. If the list is odd, it returns the original list. The test_even list is passed to the function, and the sorted version is printed.