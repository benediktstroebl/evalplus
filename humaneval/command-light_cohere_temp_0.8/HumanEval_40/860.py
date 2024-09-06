```python
def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.
    """
    def sum_three_distinct(l: list):
        return sum(set(l)) == 0
    return sum_three_distinct(l)

def sum_three_distinct(l: list):
    return sum(l) - (sum(l) - sum(set(l)))

if __name__ == "__main__":
    assert triples_sum_to_zero([1, 3, 5, 0]) is True
    assert triples_sum_to_zero([1, 3, -2, 1]) is True
    assert triples_sum_to_zero([1, 2, 3, 7]) is False
    assert triples_sum_to_zero([2, 4, -5, 3, 9, 7]) is True
    assert triples_sum_to_zero([1]) is False
    ```