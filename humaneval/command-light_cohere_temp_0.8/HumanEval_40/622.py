```python
def triples_sum_to_zero(l: list):
    if sum(map(int, l))) <= 0:
        return True
    return False

# Test the function
for i in range(0,10):
    if triples_sum_to_zero([i, i+2, i+4]) == True:
        print("YES")
    else:
        print("NO")
```

This code defines a function `triples_sum_to_zero` which takes a list of integers and returns true if there are three distinct elements in the list that sum up to zero. The function then uses the `map` to get the sum of the elements and checks if it's less or equal to 0. If the sum is zero, the function returns `True`, indicating that there are three distinct elements in the list that sum up to zero.

The function is then tested with a series of test cases, with the output printed to the console.