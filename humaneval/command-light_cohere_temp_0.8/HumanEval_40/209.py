```python
def triples_sum_to_zero(lst):
    if sum([x for x in lst if x <= 0]) == 0:
        return True
    return False

# Example usage:
if triples_sum_to_zero([1, 3, -2, 1]) == True:
    print("Three distinct elements sum to zero.")

if triples_sum_to_zero([1, 2, 3, 7]) == True:
    print("Three distinct elements sum to zero.")

if triples_sum_to_zero([2, 4, -5, 3, 9, 7]) == True:
    print("Three distinct elements sum to zero.")

if triples_sum_to_zero([1]) == False:
    print("False")
```