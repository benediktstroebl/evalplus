```python
def add(lst):
    even_odd = [el for i, el in enumerate(lst) if i % 2 == 1 and el % 2 == 0]
    return sum(even_odd)
```
This function uses a list comprehension to filter out even elements at odd indices from the input list and then uses the sum function to add these numbers. 

The function returns the sum of the even elements at odd indices in the list. 

To ensure that the function works correctly and behaves as expected, tests can be added to evaluate its performance. Below is a markdown code block with example tests to ensure the correctness of the function:
```python
# Tests:
assert add([4, 2, 6, 7]) == 2, "Failed odd indexed even element addition"
assert add([1, 3, 5, 7]) == 10, "Failed to identify odd indexed even elements"
assert add([2, 4, 6, 8, 10]) == 14, "Failed to add all odd indexed even elements"
assert add([0, 2, 4, 6, 8]) == 16, "Failed to include 0 as a even element at odd index"
``` 
These tests check the function's behavior on a variety of input lists, ensuring that the function correctly identifies even elements at odd indices and calculates the sum.