```python
def pairs_sum_to_zero(lst):
    """
    Checks if all elements in the list sum to zero.
    Returns: if there are two distinct elements that sum to zero, and False otherwise.
    """
    nums = []
    for num in lst:
        nums.append(num)
    if sum(nums) == 0:
            return True
    else:
        return False
    """

# Example usage
if pairs_sum_to_zero([1, 3, -2, 1]) == True:
    print("List has two distinct elements that sum to zero.")

if pairs_sum_to_zero([1, 2, 3, 7]) == True:
    print("List has two distinct elements that sum to zero.")

if pairs_sum_to_zero([2, 4, -5, 3, 5, 7]) == True:
    print("List has two distinct elements that sum to zero.")

if pairs_sum_to_zero([1]) == False:
    print("No two elements sum to zero.")
```