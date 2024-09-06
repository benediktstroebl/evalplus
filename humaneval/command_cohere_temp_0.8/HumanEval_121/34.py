```python
def solution(lst):
    odd_in_even = sum(x for x in lst if x % 2 and (len(lst) - x) % 2 == 0)
    return odd_in_even
```
This Python script defines a function called solution which takes a list lst as input. It uses a sum function to calculate the sum of odd numbers present in even positions in the list. The conditions for the sum are generated using the logical statements: `x % 2` to check if the element x is odd, and `(len(lst) - x) % 2 == 0` to determine if the element x is in an even position within the list. The `odd_in_even` variable captures the sum of such odd elements, and the function returns this computed sum.