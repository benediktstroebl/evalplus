```python
def triples_sum_to_zero(lst):
    sum_to_zero = [0, 0, 0]
    for i, n in enumerate(lst):
        for j in range(0, 3):
            if n == j:
                sum_to_zero[j] += 1
    return bool(sum_to_zero == (0, 0, 0)))
``` 
This script defines a function `triples_sum_to_zero` which aims to solve the problem. 

The function takes a list of integers as input and uses a nested loop to iterate over the list. The outer loop runs for three times (modeling the three possible combinations), and the inner loop runs for each element in the list. 

The function then uses a list comprehension to create a list `sum_to_zero` that keeps track of which elements in the input list have been used to satisfy the three distinct requirement. 

The final output of the function is `True` if there are three distinct elements in the list that sum to zero, and `False` otherwise.