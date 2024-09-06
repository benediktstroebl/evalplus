```python
def pairs_sum_to_zero(l):
    return sum(x+y for x,y in zip(l,l)) <= 0

#Test cases
test_sum_zero = [
    [
        ("[1, 3, 5, 0]", "False"),
        ("[1, 3, -2, 1]", "False"),
        ("[1, 2, 3, 7]", "False"),
        ("[2, 4, -5, 3, 5, 7]", "True"),
        (["1"], "False"),
        ]
    )

for case in test_sum_zero:
    assert pairs_sum_to_zero(case[1]) == case[2]
```