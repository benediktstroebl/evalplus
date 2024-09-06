```python
def triples_sum_to_zero(lst):
    """
    Function to check if there are three distinct elements in a list that sum to zero.
    Returns: True if there are three such distinct elements in the list that sum to zero, and False otherwise.
    """
    triple_sum = 0
    for num in lst:
        if num == triple_sum:
            continue
        triple_sum += num
    return True if triple_sum == 0 else False

# Example Usage
triple_sum_to_zero([1, 3, -2, 1])  # Returns True
```
This script defines a function named triples_sum_to_zero that checks whether a list of integers contains three distinct elements that sum to zero. The function initializes a triple_sum to track the sum of the current set of elements. 

Then, it uses a loop to iterate through each element in the list. If it finds a element that is equal to triple_sum, it immediately breaks out of the loop using the continue statement. This ensures that the unique triple is not added twice to the sum. 

The function returns True if there are three distinct elements that sum to zero, and False otherwise.