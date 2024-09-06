```python
def triples_sum_to_zero(lst):
    sum_to_zero = [x + y + z for x, y, z in zip(lst, lst[1:], lst[2:])]
    return sum_to_zero == [0] * 3

# Tests
 triples_sum_to_zero([1, 3, 5, 0])  # Should return True
 triples_sum_to_zero([1, 3, -2, 1])  # Should return True
 triples_sum_to_zero([1, 2, 3, 7])  # Should return False
 triples_sum_to_zero([2, 4, -5, 3, 9, 7])  # Should return True
 triples_sum_to_zero([1])  # Should return False
```
The provided Python script defines a function `triples_sum_to_zero` that aims to determine if there are three distinct elements in a list that add up to zero. The function utilizes a `zip` function to create lists of three elements (x, y, z) and then sums them up, comparing the result to `[0] * 3. The tests section further validates the the function's behavior by providing a variety of test cases.