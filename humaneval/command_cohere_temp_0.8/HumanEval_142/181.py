```python
def sum_squares(lst):
    result = 0
    for i, num in enumerate(lst):
        if i % 3 == 0:
            num **= 2
        elif i % 4 == 0 and i % 3 != 0:
            num **= 3
        result += num
    return result
```
The function sums over the list, iterating through each entry. It squares entries with index divisible by 3 and cubes entries with index divisible by 4 and not divisible by 3. The final sum is then returned. 

The provided example inputs and desired outputs are correct, and the function should output:
- 6 for lst = [1, 2, 3]
- 0 for lst = []
- -126 for lst = [-1, -5, 2, -1, -5]

This problem can be solved using basic indexing and mathematical operations. If there are multiple steps, it may be helpful to break down the problem even further to catch any edge cases that may arise. Let me know if I missed any critical details or if you'd like me to walk through a more complex example!