```python
def max_element(l: list):
    """Return maximum element in the list.
    
    Args:
        l (list): List of elements.
    
    Returns:
        int or float: Maximum element in the list.
    """
    if not l:
        raise ValueError("List cannot be empty")
    
    max_element = max(l)
    return max_element
```

The function takes a list `l` as an argument and uses the `max` function to find the maximum element in the list. It returns the maximum element and raises a `ValueError` if the input list is empty. 

To run the code, you can copy and paste it into a Python interpreter or save it as a script file (e.g., `max_element.py`) and execute it using the command line:
```bash
python max_element.py
```

This will execute the script, and if there are no syntax errors, it will output the result of the max_element function for the test cases provided in the problem statement.