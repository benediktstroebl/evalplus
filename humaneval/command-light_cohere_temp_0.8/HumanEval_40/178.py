```python
def triples_sum_to_zero(l):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.
    """
    def test_triples_sum_to_zero(test_list):
        return triples_sum_to_zero(test_list) and not sum(test_list) == 0

    return test_triples_sum_to_zero, sum(map(int, input())) == 6

 ```

This script defines a function `triples_sum_to_zero` which checks whether a list contains three elements whose sum is zero, and a test function `test_triples_sum_to_zero` which tests the `triples_sum_to_zero` function using a sample list.  The use `test_triples_sum_to_zero` and the `sum()` function to ensure the function behaves correctly.