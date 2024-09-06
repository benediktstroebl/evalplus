```python
def max_element(l: list) -> int:
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    return max(l)
```
This Python script defines a function called `max_element` that takes a list `l` as input and returns the maximum element in the list. The function uses the `max` function to compare and return the highest value in the list.

The script includes example test cases in the function signature, which are designed to verify the correctness of the function. These test cases are generated dynamically and do not require specific inputs to be provided in the comments.

The function is designed to be self-contained and easy to use, and it can be used to efficiently find the maximum element in any given list. 

It is important to ensure that the max function is imported in the Python script to ensure the correct operation of the max_element function. This import statement is typically added at the beginning of the script, before the function definition:
```python
import max
``` 
 clarifying that the max function is imported from the built-in max module and not an intentional typo in the previous response.