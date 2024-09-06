```python
def triples_sum_to_zero(l):
    if sum([x for x in l if x <= 0]) == 0:
        return True
    return False

# Unit tests
test_triples_sum_to_zero = []
test_triples_sum_to_zero.add([range(0, 4), [1, 3, -2, 1])
test_triples_sum_to_zero.add([range(0, 5), [2, 4, -5, 3, 9, 7]))
test_triples_sum_to_zero.add([range(0, 6), [2, 4, -5, 3, 8, 7, 6))

test_triples_sum_to_zero.insert(function(test_triples_sum_to_zero[0]))
print(test_triples_sum_to_zero)

test_triples_sum_to_zero.insert(function(test_triples_sum_to_zero[1]))
print(test_triples_sum_to_zero)

test_triples_sum_to_zero.insert(function(test_triples_sum_to_zero[2]))
print(test_triples_sum_to_zero)

test_triples_sum_to_zero.insert(function(test_triples_sum_to_zero[3]))
print(test_triples_sum_to_zero)
```