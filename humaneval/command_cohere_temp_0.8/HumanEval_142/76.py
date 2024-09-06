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

The script uses a for loop to iterate through each index and corresponding value in the input list `lst`. The `enumerate` function is used to access the index `i` and the value `num` simultaneously. The code then checks if the index `i` is a multiple of 3 or 4 using the modulo operator `%`. 

If the index is a multiple of 3, the value is squared `**= 2`. If the index is a multiple of 4 but not a multiple of 3, the value is cubed `**= 3`. The modified value is then added to the running total `result`. Finally, the function returns the modified sum. 

This code solves the problem in a self-contained manner, as it doesn't rely on any external variables or functions and can be run independently. 

To make the code even more concise, you can use the `sum` and `map` functions to create a conciseGolfier version:
```python
sum(map(lambda x: x**(i%2+1), lst))
```

In this version, a lambda function is used to dynamically raise the element `x` to the power of the modulo result `i%2+1`, where `i` is the index of the list element. The `map` function applies this lambda function to each element in the list `lst`, and the result is summed using the `sum` function. This provides an elegant and concise solution to the problem.