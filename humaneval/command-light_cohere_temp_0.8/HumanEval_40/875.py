```python
def triples_sum_to_zero(l):
    if sum(map(item<2>, l)) == 0:
        return True
    return False

# Test the function with given input
if __name__ == "__main__":
    assert triples_sum_to_zero([1, 3, 5, 0]) == True
    assert triples_sum_to_zero([1, 3, -2, 1]) == True
    assert triples_sum_to_zero([1, 2, 3, 7]) == False
    assert triples_sum_to_zero([2, 4, -5, 3, 9, 7]) == True
    assert triples_sum_to_zero([1]) == False
    ```