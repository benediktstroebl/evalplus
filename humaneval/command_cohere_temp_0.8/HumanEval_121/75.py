```python
def solution(lst):
    odd_in_even = sum(x for i, x in enumerate(lst) if i % 2 == 1 and x % 2 == 1)
    return odd_in_even
```
This Python script defines a function called solution which takes a list lst as input. It uses a sum function to calculate the sum of odd numbers found in even positions in the list. The enumerate function is used to iterate through the list, and the index i is used to determine whether the element is in an even position (i % 2 == 1). At the same time, the element itself is checked to see if it's odd (x % 2 == 1). The sum is then calculated for the odd numbers in even positions and returned as the result. This solution is implemented as a standalone function, meaning it can be executed directly without the need for external dependencies or additional code.