```python
def sum_squares(lst):
    """
    Return the sum of squared integers in the list.
    
    Args:
        lst (list): A list of numbers.
    
    Returns:
        int: The sum of squared integers rounded up to the next integer.
    """
    result = 0
    for num in lst:
        if isinstance(num, float) or isinstance(num, complex):
            continue
        num = int(num)
        result += num ** 2
    
    return int(result)
```

The function iterates through each element in the list `lst`. It checks if the element is either an instance of `float` or `complex`. If so, it skips that element and moves to the next iteration. Otherwise, the element is squared, added to the `result` variable, and returned after being converted to an integer. 

This way, the code makes sure to only calculate the sum of squared integers, as per the problem statement. 

To use this function, just import it in your Python script and call it with a list of inputs. Here is an example:
```python
import sum_squares

print(sum_squares.sum_squares([1, 2, 3]))  # Output: 14
``` 
This will print out `14`, which is the sum of the squares of integers in the list `[1, 2, 3]`, rounded up to the next integer.