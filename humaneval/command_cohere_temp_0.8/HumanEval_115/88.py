Here's a Python script that solves the problem using a nested `for` loop and the `math.ceil()` function to calculate the maximum number of times you need to lower the bucket, along with a concise explanation of how the solution works:
```python
import math

def max_fill(grid, capacity):
    filled_rows = 0
    max_fillings = 0

    for row in grid:
        filled_rows += row.count(1)

        max_fillings = max(
            max_fillings,
            math.ceil(filled_rows / capacity)
        )

    return max_fillings
```

**Explanation:**
1. We initialize `filled_rows` to count how many rows contain any filled wells (with a value of `1`).
2. We also initialize `max_fillings` to keep track of the maximum number of fillings needed over all rows.
3. We use a `for` loop to iterate through each row in the `grid`.
4. For each row, if a well is filled (`1` in the row), we increment `filled_rows` by 1.
5. We use the `math.ceil()` function to calculate the maximum number of times we need to dip the bucket into the wells to empty them. This is done by dividing the total filled rows by the capacity of the bucket.
6. We take the maximum between the current `max_fillings` and the calculated fillings needed for the current row.
7. After iterating through all rows, we return the final `max_fillings` value.

The script's solution is consistent with the approach discussed previously, ensuring that it fulfills the problem's requirements.