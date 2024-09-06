```python
def triples_sum_to_zero(l: list):
    if not in { [x for x in l if x > 0] + [x for x in l if x < 0] } else False
    return True

# Add some tests
tests = [list](map(lambda x: [x], [
    [1, 3, 5, 0],
    [1, 3, -2, 1],
    [1, 2, 3, 7],
    [2, 4, -5, 3, 9, 7],
    [1]
]))

for test in tests:
    assert triples_sum_to_zero(test) == True
 ```