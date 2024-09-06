```python
def will_it_fly(q, w):
    return (sum(q) <= w) and (w == q[0] + q[-1] == sum(q[1:-1]) or w == sum(q))
```

The function uses the sum reconciliation technique to check if the list of numbers is balanced or not. If the sum of the numbers is equal to the total then it is necessarily balanced. Otherwise, the sum of the numbers is equal to the sum of the first element, the last element and the rest of the elements in the list (except the first and last). Thus, the answe is true if the sum of the elements of the list is less than or equal to the maximum possible weight and the list is balanced. 

This is done during each iteration of a nested loop in the provided test cases and for every new test case the user can input. This allows for proper edge case testing of the function.