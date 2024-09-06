```python
def pairs_sum_to_zero(l):
    # Go through each element and find its pair
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[i] + l[j] == 0:
                return True
    return False
```

This algorithm uses two nested loops to iterate through all possible pairs of elements in the list and checks if their sum is zero. The code efficiently checks all pairs and returns 'True' if any pair sums up to zero, and 'False' otherwise. 

This solution passes the unit tests provided in the prompt, as well as additional tests:
```
>>> pairs_sum_to_zero([1, 3, 5, 0])
False
>>> pairs_sum_to_zero([1, 3, -2, 1])
False
>>> pairs_sum_to_zero([1, 2, 3, 7])
False
>>> pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
True
>>> pairs_sum_to_zero([1])
False
>>> pairs_sum_to_zero([10, 20, 30, 40, 50])
False
>>> pairs_sum_to_zero([1, 2, 3, 10, 11, 12])
False
``` 
It is worth noting that the algorithm's time complexity is O(n^2) since it uses two nested loops, which might make it less efficient for large input lists. However, the simplicity of the algorithm makes it comprehensible and easy to maintain.