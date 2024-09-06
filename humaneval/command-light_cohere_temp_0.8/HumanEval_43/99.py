```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
>> pairs_sum_to_zero([1, 3, 5, 0])
return False
>>
```
This approach uses a dictionary of common pairs to check if there are two elements that sum up to zero.

A possible solution:
```python
def pairs_sum_to_zero(l):
    s = set()
    for num in l:
        if num in s: return False
        s.add(num)
    return True
    return False
```