```python
def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.
    """

    l = [1,3,5,0]
    print(triples_sum_to_zero(l))  # Should print True
    l = [1,2,3,7]
    print(triples_sum_to_zero(l))  # Should print False
    l = [2,4,-5,3,9,7]
    print(triples_sum_to_zero(l))  # Should print True
    ```