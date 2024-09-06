Here's a Python script that includes a function to solve the given problem:
```python
def add_elements(arr, k):
    sum_two_digits = sum(int(d) for d in map(str, arr) if len(d) <= 2)
    return sum_two_digits // k if k != 1 else sum_two_digits

# Example usage
arr = [111, 21, 3, 4000, 5, 6, 7, 8, 9]
k = 4
result = add_elements(arr, k)
print(f"Example output: {result}")

```

The function `add_elements` takes an array `arr` and an integer `k` as inputs. It uses a generator expression to sum up the elements whose representation has at most two digits. If `k` is not equal to 1, the sum is divided by `k` to account for the duplicate counting.