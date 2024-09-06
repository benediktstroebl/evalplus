```python
def solution(lst):
    odd_in_even = sum(x for i, x in enumerate(lst) if i % 2 == 1 and x % 2 == 1)
    return odd_in_even
```
This Python script defines a function called solution which takes a list lst as input. It uses a sum function to calculate the sum of odd numbers found in even positions in the list. The enumeate function allows us to iterate over the list using the enumerate function, which assigns each element a number (index). It calculates the sum of odd-position elements if the list index is also odd, returning the sum of all odd numbers in even positions in the list. In essence, it solves the problem posed in the code block.