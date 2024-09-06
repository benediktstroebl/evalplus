```python
def triples_sum_to_zero(l):
    return any(sum(x) <= 0 for x in l)

# Test the function
test_triples_sum_to_zero = []
test_triples_sum_to_zero.append([1, 3, -2, 1])
test_triples_sum_to_zero.append([1, 2, 3, 7])
test_triples_sum_to_zero.append([2, 4, -5, 3, 9, 7])
test_triples_sum_to_zero.append([1])
test_triples_sum_to_zero.append([3, 7])
test_triples_sum_to_zero.append([4])
test_triples_sum_to_zero.append([5, 8])

def test_function(test_list):
    test_triples_sum_to_zero(test_list)

test_function(test_triples_sum_to_zero)
```