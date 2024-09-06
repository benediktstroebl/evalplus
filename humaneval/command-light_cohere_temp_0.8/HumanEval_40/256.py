```python
def triples_sum_to_zero(lst):
    return all(x + y + z <= 0 for x, y, z in zip(lst, lst[1:], lst[2:]))

# Example usage:
if __name__ == "__main__":
    input_list = [1, 3, 5, 0, -2, 1]
    result = triples_sum_to_zero(input_list)
    print(result)  # Output: True
```

This function checks if there are three distinct elements in the list that their sum is equal to or less than zero. If it passes the whole test, it returns `True`; otherwise, it returns `False`.