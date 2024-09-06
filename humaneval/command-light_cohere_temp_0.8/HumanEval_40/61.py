```python
def triples_sum_to_zero(lst):
    # Initialize variables
    sum_positive = 0
    sum_negative = 0
    sum_zero = 0

    # Iterate through list
    for num in lst:
        if num > 0:
            sum_positive += num
        elif num < 0:
            sum_negative += num
        else:
            sum_zero += num

    # Check conditions
    if sum_positive == 0 and sum_negative == 0 and sum_zero == 0:
        return True
    else:
        return False
```
The above code defines a Python function named triples_sum_to_zero that aims to determine if there are three distinct elements in a list that sum to zero. It uses a specific conditions to check if the list satisfies this property. 

It then returns 'True' if all three conditions hold true, indicating that the list contains three elements that sum to zero, and 'False' otherwise.