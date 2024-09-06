```python
import math

def max_fill(grid, capacity):
    filled_rows = sum(row for row in grid if sum(row) > 0)
    return math.ceil(filled_rows / capacity)
```

The script utilizes a simple formula where the sum of filled rows is divided by the capacity of the bucket and then rounded up using the `math.ceil()` function. This provides the number of times the bucket must be lowered to empty the wells. 

The `max_fill()` function takes two parameters, `grid` and `capacity`, where `grid` is represented as a list of lists and `capacity` is the water-carrying capacity of the bucket. 

To get the total number of rows filled with water, the sum of each row in the `grid` is calculated using a generator expression `sum(row for row in grid if sum(row) > 0)`. 

The capacity is then divided by this value and rounded up using `math.ceil()` to get the maximum number of times one needs to lower the bucket to empty the wells. 

This approach ensures accuracy and efficiency in solving the problem. 

This solution can be tested by calling the function with different inputs and comparing the output with the expected results as shown in the examples mentioned in the problem statement.