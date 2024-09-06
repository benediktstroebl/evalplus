```python
def add(lst):
    even_odd = [el for i, el in enumerate(lst) if i % 2 == 1 and el % 2 == 0]
    return sum(even_odd)
```
This function uses a list comprehension to filter out even elements at odd indices from the input list and then uses the `sum()` function to add these numbers. 

Here is a self-contained Python script that utilizes the function above:
```python
def add(lst):
    even_odd = [el for i, el in enumerate(lst) if i % 2 == 1 and el % 2 == 0]
    return sum(even_odd)

# Test Cases
assert add([4, 2, 6, 7]) == 2
assert add([1, 3, 5, 7]) == 5 
assert add([0, 2, 4, 6, 8]) == 8 
```
You can add more test cases to verify the function under different scenarios.