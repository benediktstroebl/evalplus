```python
def get_positive(l: list):
    return [x for x in l if x > 0]
```

The function utilizes a list comprehension with a condition stating `x > 0` to filter out any positive numbers from the provided list `l`. As the list comprehension returns a new list, this will be the output of the function. 

The problem states that the function should only return the positive numbers in the list, and the unit tests provide to verify this requirement are `[5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]`. 

This is an example of how the function can be used in action:
```python
# Example usage
input_list = [-1, 2, -4, 5, 6]
print(get_positive(input_list))  # Expected output: [2, 5, 6]
``` 

This produces the desired output of `[2, 5, 6]`. 
If you wish, we can compile some more scenarios to test the function; feel free to ask if you have any more questions or comments!