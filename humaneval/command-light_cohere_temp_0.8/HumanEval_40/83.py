```python
def triples_sum_to_zero(lst):
    """
    function to find 3 distinct elements sum to 0
    """
    set = set()
    for num in lst:
        if set.add(num):
            return False
    return True
  ```