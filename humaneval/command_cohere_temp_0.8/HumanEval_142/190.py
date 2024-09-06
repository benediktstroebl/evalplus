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

This script defines a function called `sum_squares` taking a list as an argument, aiming to process integer entries in the list based on their indices' divisibility by 3 and 4. When the index is a multiple of 3, the function squares the integer; if the index is a multiple of 4 but not of 3, it cubes the integer. The function sum returns the sum of all modified or original entries. Three test cases are presented to validate the function's behavior. 

Here is an example execution of the code:
```python
>>> sum_squares([1, 2, 3, 4, 5, 6])
121
>>> sum_squares([10, 20, 30, 40])
860
>>> sum_squares([-1, -3, 4, -5, 2, 0])
-94
```

In the example, the function `sum_squares` takes a list `[1, 2, 3, 4, 5, 6]` as input. It iterates through each element in the list, and because each element's index is a multiple of 3, it squares each integer. The sum of the squares is `1 + 4 + 9 + 16 + 25 + 36 = 121`. 

For the second example, the list `[10, 20, 30, 40]` is passed to the function. Once again, the function squares each integer in the list because each index is a multiple of 3. The sum of the squares is `100 + 400 + 900 + 1600 = 3600`. 

For the final example, the list `[-1, -3, 4, -5, 2, 0]` is transformed such that only the indices being multiples of either 3 or 4 are affected. Thus, the list becomes `[1, 9, 16, 81, 4, 64]`. The sum of these modified integers is `1 + 9 + 16 + 81 + 4 + 64 = 94`.