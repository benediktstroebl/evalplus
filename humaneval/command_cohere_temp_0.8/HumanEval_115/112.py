Here's a Python script that solves the problem using a nested loops approach:
```python
import math

def max_fill(grid, capacity):
    filled_rows = 0
    max_fill = 0

    # Iterate through each row in the grid
    for row in grid:
        filled_cells = 0

        # Count filled cells in the current row
        for cell in row:
            if cell == 1:
                filled_cells += 1

        # Calculate the maximum water that can be fetched from the current row
        max_fill = max(filled_cells, max_fill)

        # If the number of filled cells is equal to the capacity, consider it a filled row
        if filled_cells == capacity:
            filled_rows += 1

    return filled_rows + max_fill

# Example Usage
grid = [[0, 0, 1, 0], [0, 1, 0, 0], [1, 1, 1, 1]]
capacity = 1
result = max_fill(grid, capacity)
print(result)  # Output: 6
```
This approach iterates through each cell in the grid and for each row, counts the number of filled cells to calculate the maximum amount of water that can be fetched from that row. Then, it checks if the number of filled cells in the entire row equals the capacity, in which case it considers the row filled and increments the count of filled rows. The total number of buckets lowered is determined by adding the count of filled rows to the maximum fill count.