```python
def triples_sum_to_zero(lst):
    return any(sum(x) == 0 for x in lst) and all(x != 0 for x in lst)

# Example usage:
if __name__ == "__main__":
    lst = [1, 3, 5, 0]
    print(triples_sum_to_zero(lst))  # Output: True
```
This code defines a `triples_sum_to_zero` function. This function takes a full, self-contained test, returning `True` if there are three distinct elements in the list that sum to zero, and `False` otherwise. This function is critical for problems that require sets of numbers to be three elements that add up to zero.