```python
def triples_sum_to_zero(lst):
    if sum(set(map(int, lst))) == 0:
        return True
    return False

# Test suite
tests = [
    "olds" = [1, 3, 5, 0]
    "new" = [1, 3, -2, 1]
    "odd" = [2, 4, -5, 3, 9, 7]
    assert triples_sum_to_zero("olds") == False
 assert triples_sum_to_zero("new") == True
 assert triples_sum_to_zero("odd") == False
```