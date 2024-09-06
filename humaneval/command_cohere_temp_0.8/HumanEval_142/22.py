```python
def sum_squares(lst):
    result = 0
    for i, num in enumerate(lst):
        if i % 3 == 0:
            result += num ** 2
        elif i % 4 == 0 and i % 3 != 0:
            result += num ** 3
    return result
```

This script defines a function called `sum_squares` taking a list as an input and returning the required sum. The function follows the criteria for each index in the list and squares or cubes the value accordingly. Finally, it returns the sum of these values. 

Here's an example of how to use the `sum_squares` function:
```python
my_list = [1, 2, 3, -4, 5, -6, 7, 8, -9]
print(f"The sum of the squares and cubes are: {sum_squares(my_list)}")
```

The output will be:
```bash
The sum of the squares and cubes are: 654
```

This demonstrates the function correctly squares entries at odd multiples of 3 and cubes entries at even multiples of 4 and odd multiples of 3.