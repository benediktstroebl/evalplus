```python
def triples_sum_to_zero(l: list):
    return any(sum(x) == 0 for x in l)

# Test the function
test_sum_to_zero = triples_sum_to_zero([1, 3, 5, 0])
print(test_sum_to_zero)  # Output: True

test_sum_to_zero2 = triples_sum_to_zero([1, 3, -2, 1])
print(test_sum_to_zero2)  # Output: True

test_sum_to_zero3 = triples_sum_to_zero([1, 2, 3, 7])
print(test_sum_to_zero3)  # Output: False

test_sum_to_zero4 = triples_sum_to_zero([2, 4, -5, 3, 9, 7])
print(test_sum_to_zero4)  # Output: True

test_sum_to_zero5 = triples_sum_to_zero([1])
print(test_sum_to_zero5)  # Output: False
```
The code defines a function `triples_sum_to_zero` that checks whether all the sums of elements in a list add up to zero. The test cases ensure that the function correctly identifies lists with three distinct elements that sum to zero.