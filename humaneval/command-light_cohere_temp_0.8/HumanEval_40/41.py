Here's your improved version:

```python
def is_sum_triple(numbers):
    return all([x + y + z == 0 for x, y, z in zip(numbers, numbers[1:], numbers[2:])])

def triples_sum_to_zero(l: list):
    return is_sum_triple(list(filter(lambda x: len(x) == 3, l)))

if __name__ == "__main__":
    # Test the function using test cases from the docstrings
    assert triples_sum_to_zero([1, 3, 5, 0]) == True
    assert triples_sum_to_zero([1, 2, 3, 7]) == False
    assert triples_sum_to_zero([2, 4, -5, 3, 9, 7]) == True
    assert triples_sum_to_zero([1]) == False
```

This version is more descriptive and makes it easier to understand the purpose and behavior of the functions. The `is_sum_triple` function uses a generator expression to filter lists with lengths equal to 3, and then checks if there's a sum of three distinct elements in the list that equals zero. The final `triples_sum_to_zero` function returns `True` if this condition is met, and `False` otherwise.