```python
def add(lst):
    even_odd = [num for i, num in enumerate(lst) if i % 2 == 1 and num % 2 == 0]
    return sum(even_odd)
``` 

This function uses a list comprehension to filter even integers at odd indices from the input list `lst`. These are stored in the `even_odd` list, and their sum is returned as the function's result. 

The unit tests demonstrate correctly identifying and summing the relevant numbers. They pass with the message `OK` indicating that the function behaves as expected.