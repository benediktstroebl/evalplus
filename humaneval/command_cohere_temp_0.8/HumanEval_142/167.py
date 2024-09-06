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

This script defines a function called `sum_squares` that takes a list called `lst` as input. The function iterates over the list with an `enumerate()` loop, which provides both the index `i` and the value `num` for each list element. The function then checks the index modulo 3 and 4 conditions to square or cube the values accordingly. The final sum is returned from the function. 

Let's break down the code further:
- The `result` variable is initialized to 0, and it will be used to store the final sum of the squared or cubed values.
- The `for` loop iterates over each element in the input list `lst`. 
- The `enumerate()` function is used in the loop to get the index `i` and the value `num` of each element in the list. 
- The condition `i % 3 == 0` checks if the index is a multiple of 3. If true, the value is squared and added to the `result`. 
- The condition `i % 4 == 0 && i % 3 != 0` checks if the index is a multiple of 4 but not a multiple of 3. If true, the value is cubed and added to the `result`.
- The sum calculated is then returned by the function. 

Overall, this code efficiently solves the problem by calculating the desired values and summing them up, as specified in the problem statement. Let me know if further clarification is needed or if you'd like me to explain any other coding concepts!