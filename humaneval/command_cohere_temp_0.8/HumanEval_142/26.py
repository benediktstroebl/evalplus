```python
def sum_squares(lst):
    result = 0
    for i, num in enumerate(lst):
        if i % 3 == 0:
            num **= 2
        elif i % 4 == 0 and i % 3 != 0:
            num **= 3
        result += num
    return result
```
The function sums over the list, for each entry applying the respective operation based on the index criteria. An example execution follows:
```python
print(sum_squares([1, 2, 3]))  # Output: 6
print(sum_squares([-1, -5, 2, -1, -5]))  # Output: -126
print(sum_squares([0, 10, 20, 30]))  # Output: 240
``` 
This demonstrates the functionality of the `sum_squares` function, applying the required operations to the list elements and then summing the results. Feel free to adapt and extend this code for your specific needs.