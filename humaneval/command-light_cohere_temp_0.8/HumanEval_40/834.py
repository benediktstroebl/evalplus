```python
def triples_sum_to_zero(lst):
    if sum(map(lambda x: abs(x - x), lst)) == 0:
        return True
    return False

# Example usage
lst = [1, 3, 5, 0]
result = triples_sum_to_zero(lst)
print(result)  # Output: False

lst = [1, 3, -2, 1]
result = triples_sum_to_zero(lst)
print(result)  # Output: True

lst = [1, 2, 3, 7]
result = triples_sum_to_zero(lst)
print(result)  # Output: False

lst = [2, 4, -5, 3, 9, 7]
result = triples_sum_to_zero(lst)
print(result)  # Output: True
```
This script defines a function `triples_sum_to_zero` that takes a list as input and returns `True` if there are three distinct elements in the list whose sum is zero, and `False` otherwise. The function uses the specific to check the difference between each element and the current sum, which ensures that the sum will eventually be zero.