Here's a Python script that solves the problem using a nested for loop and a `sum` function:
```python
import math

def max_fill(grid, capacity):
    filled_rows = sum(sum(row) for row in grid)
    return math.ceil(filled_rows / capacity)

# Example usage
grid1 = [ [0,0,1,0], [0,1,0,0], [1,1,1,1] ]
print(max_fill(grid1, 1))
# Output: 6

grid2 = [ [0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1] ]
print(max_fill(grid2, 2))
# Output: 5
```

The function `max_fill` takes a 2D array `grid` and an integer `capacity` as input, the sum of values in each row is calculated using the `sum` function and the total number of rows is calculated using a nested sum. Then, the total number of bucket fillings is calculated by dividing the total water by the bucket capacity and rounding up using the `math.ceil` function. The function correctly handles the cases for any rectangular grid of wells with 0s and 1s representing units of water, and any valid bucket capacity. 

Note that this solution makes use of Python 3 features, especially the simplified summary using `sum` and a more concise map-style outline for the function header. If you are targeting Python 2, you may need to rewrite the solution accordingly. 
Let me know if you'd like to have it modified for Python 2.  Also, if you'd like to explore alternative solutions, we can generate one using list comprehensions or optimized nested loops, etc.