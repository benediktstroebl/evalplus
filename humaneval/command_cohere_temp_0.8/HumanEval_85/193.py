```python
def add(lst):
    even_odd = [el for i, el in enumerate(lst) if i % 2 == 1 and el % 2 == 0]
    return sum(even_odd)
```
This function uses a list comprehension to filter out even elements at odd indices from the input list and then uses the `sum()` function to add these numbers. 

Here is a usage example of the `add()` function:
```python
print(add([4, 2, 6, 7]))  # Output: 2
``` 
This would print the expected result of 2, which is the sum of the even elements at odd indices in the list `[4, 2, 6, 7]`.