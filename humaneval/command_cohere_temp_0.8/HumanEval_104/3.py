Here's a Python script that contains a function called unique_digits, which solves the problem you've described:
```python
def unique_digits(xs):
    """Return sorted list of elements in xs that have no even digits."""
    result = [x for x in xs if not any(int(y) % 2 == 0 for y in str(x))]
    return sorted(result)

# Tests:
print(unique_digits([15, 33, 1422, 1]))  # Output: [1, 15, 33]
print(unique_digits([152, 323, 1422, 10]))  # Output: []
```
This script defines the `unique_digits` function, which takes a list of positive integers as input (`xs`) and returns a sorted list of elements that contain no even digits. The function includes an explanation that is consistent with the problem statement.

The script also includes a pair of test cases that will print the expected output of the function when provided with the respective inputs. Adjust the test cases as needed to match the problem's guidelines.