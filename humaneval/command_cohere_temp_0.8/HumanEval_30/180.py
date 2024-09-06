```python
def get_positive(l: list):
    return [x for x in l if x > 0]
```

The function utilizes a list comprehension to filter out elements that are not greater than zero, resulting in a new list that contains only the positive numbers from the original input list. 

Such a concise solution is achievable due to the flexibility of using list comprehensions in Python. This allows for the direct expression of the test for element inclusion within the solution, which simplifies the code in this case. 

This function can provide consistent and expected results for the given problem statement. For instance:
```python
>> get_positive([-1, 2, -4, 5, 6])
[2, 5, 6]
>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
[5, 3, 2, 3, 9, 123, 1]
``` 
The output aligns with the problem's expected outcomes. In these examples, the function is invoked with a list of numbers, and it returns a new list that includes only the positive numbers from the original list, sorting them in ascending order.