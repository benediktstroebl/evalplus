```python
def add(lst):
    even_odd = [num for i, num in enumerate(lst) if i % 2 == 1 and num % 2 == 0]
    return sum(even_odd)
``` 

This function uses a list comprehension to filter even integers at odd indices from the input list `lst`. These are stored in the `even_odd` list, and their sum is returned as the function's result. 

The problem statement asks to return the sum of these even integers, but the provided code returns a list of these numbers. 
To solve the problem as requested, you can use the `sum()` function to calculate the sum of the elements in the `even_odd` list, and modify the function to return the result, as follows: 

```python
def add(lst):
    even_odd = [num for i, num in enumerate(lst) if i % 2 == 1 and num % 2 == 0]
    return sum(even_odd)
``` 

This function now correctly satisfies the prompt's requirements. It returns the sum of even elements at odd indices in the given list.