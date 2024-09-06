```python
def add(lst):
    even_odd = [val for i, val in enumerate(lst) if i % 2 == 1 and val % 2 == 0]
    return sum(even_odd)
``` 

This function solves the problem statement by filtering out even integers that are situated at odd indices from the list and then summing them returning the result. 

Note that this code assumes that the list elements are integers. If the list contains other data types, the function may not work as expected. 

Test cases that establish the correct operation of the function are also vital. The test cases should cover different scenarios, including edge cases, to ensure the function's robustness.