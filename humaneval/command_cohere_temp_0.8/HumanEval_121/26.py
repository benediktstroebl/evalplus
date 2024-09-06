```python
def solution(lst):
    odd_in_even = sum(x for i, x in enumerate(lst) if i % 2 == 1 and x % 2 == 1)
    return odd_in_even
```
This Python script defines a function called solution which takes a list lst as input. It uses a sum function to calculate the sum of odd numbers found in even positions in the input list. The conditional loop enums the elements in the list and adds them to the odd_in_even variable if the current index is odd and the element itself is also odd. Finally, it returns the computed odd_in_even sum, as specified in the problem statement.