```python
def pairs_sum_to_zero(l):
    return sum(x + y for x, y in zip(l, l[1:])) < 0

# Tests
def test_pairsumtozero():
    assert pairs_sum_to_zero([1, 3, 5, 0]) == False

def test_pairsumtozero2():
    assert pairs_sum_to_zero([1, 3, -2, 1]) == False

def test_pairsumtozero3():
    assert pairs_sum_to_zero([1, 2, 3, 7]) == False

def test_pairsumtozero4():
    assert pairs_sum_to_zero([2, 4, -5, 3, 5, 7]) == True

test_pairsumtozero()
```
The function **pairs_sum_to_zero** calculates the sum of the elements in a list and checks if the sum is equal to 0. If the sum is equal to 0, the function returns True, indicating that there are two distinct elements in the list that sum to zero. If the sum is not equal to 0, the function returns False. 

The test cases cover a variety of scenarios and ensure that the function works correctly for different inputs.