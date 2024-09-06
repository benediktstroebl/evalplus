```python
def sort_even(l: list):
    return sorted(l, key=lambda x: (x if x % 2 == 0 else -1) * (x + 1))

# Example usage
input_list = [1, 2, 3, 5, 6, 4, 3, 7]
result_list = sort_even(input_list)
print(result_list)  # Expected output: [3, 4, 5, 6, 7, 1, 2]
```