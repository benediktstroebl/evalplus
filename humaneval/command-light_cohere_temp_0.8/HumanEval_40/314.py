Here's a self-contained Python function that solves the problem of finding three distinct elements in a list that sum to zero:
```python
def triples_sum_to_zero(l: list):
    n = len(l)
    for i in range(n):
        for j in range(i + 1, n):
            sum_check = l[i] + l[j]
            if sum_check < 0:
                return False
    return True
```
This function takes a list l as input and iterates through all possible pairs of elements using two nested loops. It calculates the important pair's sum and checks if the sum is less than zero, indicating that the elements are not distinct. If a sum is negative, the function immediately returns False, indicating that there are no three distinct elements that sum to zero. 

If the function completes its iteration without finding three distinct elements that sum to zero, it returns True.