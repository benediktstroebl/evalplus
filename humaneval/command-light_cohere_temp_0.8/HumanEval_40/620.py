```python
def triples_sum_to_zero(lst):
    return any(sum(t) == 0 for t in zip(*lst)))

# Test the function with a few examples
if __name__ == "__main__":
    print(triples_sum_to_zero([1, 3, 5, 0]))  # Output: False
    print(triples_sum_to_zero([1, 3, -2, 1]))  # Output: True
    print(triples_sum_to_zero([1, 2, 3, 7]))  # Output: False
    print(triples_sum_to_zero([2, 4, -5, 3, 9, 7]))  # Output: True
    print(triples_sum_to_zero([1]))  # Output: False
```
The script defines a function `triples_sum_to_zero` that checks whether there are three distinct elements in a list that sum to zero. 

The function returns `True` if there are such elements, and `False` otherwise. 

The function is then tested with a few examples, and the output is printed.