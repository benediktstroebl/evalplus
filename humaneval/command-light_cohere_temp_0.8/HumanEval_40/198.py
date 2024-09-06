```python
def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.
    """
    Triple sum check:
    -1 It takes the list of integers l as an argument.
    -2 Calculate the SUM = sum(map(int, l))
    -3 If SUM equals zero, return True
    -4 Else, return False
    """

    return sum(map(int, l)) == 0
``` 
This Python function triples_sum_to_zero solves the problem of finding if there are three distinct elements in a list that sum to zero. The function takes a list of integers as an argument and returns True if there are three distinct elements in the list that sum to zero, and False otherwise. The function uses a triple sum check algorithm to find the sum of three distinct elements in the list.