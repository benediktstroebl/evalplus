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

The code uses a simple loop to iterate through each list item. If the index is a multiple of 3, the item is squared; if the index is a multiple of 4 but not 3, the item is cubed. The sums are then added together and returned. 

To ensure clarity and readability, it's good practice to include descriptive variable names, such as `result` and `num` in this code, especially for more complex programs where code comprehension is of greater importance. 

Let me know if I can provide further improvements or changes to the code!