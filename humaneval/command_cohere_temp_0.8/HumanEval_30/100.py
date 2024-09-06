Here's a Python script with a self-contained function that solves the problem:
```python
def get_positive(l):
    return [x for x in l if x > 0]
```
This function uses a list comprehension, which is a compact way of creating a new list based on existing lists. In this case, it creates a new list that includes only the elements of l that are greater than zero. The expression x for x in l if x > 0 generates a list of all items x in the list l if x is greater than zero.

To test this function, you can call it with any list of integers, and it will return a list containing only the positive integers from that list. Here's an example:
```python
result = get_positive([-1, 2, -4, 5, 6])
print(result)  # Output: [2, 5, 6]
```
Here is another example:
```python
result = get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
print(result)  # Output: [5, 3, 2, 3, 9, 123, 1]
```
As expected, the function returns a list containing only the positive numbers from the input list.