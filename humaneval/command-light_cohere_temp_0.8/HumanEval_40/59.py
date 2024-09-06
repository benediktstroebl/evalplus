```python
def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.
    """
    sum of all three elements = sum(x for x in l if len(set(x)) == 3)
    if sum == 0:
        return True
    else:
        return False
    """

def test():
    """
    test_ triples_sum_to_zero([1, 3, 5, 0])
    assert triples_sum_to_zero([1, 3, 5, 0]) == False
    assert triples_sum_to_zero([1, 2, 3, 7]) == False
    assert triples_sum_to_zero([2, 4, -5, 3, 9, 7]) == True
    assert triples_sum_to_zero([1]) == False
    """

if __name__ == "__main__":
    test()
```
The function `triples_sum_to_zero` takes a list of integers and returns `True` if the list has three distinct elements that sum to zero, and `False` otherwise. The function uses the  the `sum` function to calculate the sum of the list's elements, and then checks if the sum is equal to zero.