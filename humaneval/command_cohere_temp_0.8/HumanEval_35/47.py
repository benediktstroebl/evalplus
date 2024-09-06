```python
def max_element(l: list) -> int:
    """Returns the maximum element in the list."""
    return max(l)
``` 

This code defines a function called `max_element` that takes a list `l` as input and returns the maximum element in the list. The `max` built-in function is used to determine the maximum value in the list, which is the element that appears most frequently in the list or is the highest value in the list. 

This solution is straightforward and efficient, as it uses a built-in function to solve the problem. 

Here is an example of how to use this function:
```python
print(max_element([1, 2, 3]))  # 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # 123
```
This will output:
```bash
3
123
```
Which demonstrates that the function finds the maximum element in the given lists accordingly.