```python
def get_positive(l: list):
    return [num for num in l if num >= 0]

# Test the function
test_get_positive = get_positive([-1, 2, -4, 5, 6])
assert test_get_positive == [2, 5, 6]

test_get_positive2 = get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
assert test_get_positive2 == [5, 3, 2, 3, 9, 123, 1]
```
This script defines a function `get_positive` that returns a list of positive numbers from the input list, and then tests the function's output and behavior for different inputs. The code is concise, self-contained, and easy to read, and follows good coding practices.