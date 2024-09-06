```python
def solution(lst):
    odd_in_even = sum(x for i, x in enumerate(lst) if i % 2 == 1 and x % 2 == 1)
    return odd_in_even
```
This Python script defines a function called solution which takes a list lst as input. It uses a sum function to calculate the sum of odd numbers found in even positions in the list. The conditions i % 2 == 1 and x % 2 == 1 are used to determine if a number is in an even position and if the number is odd, respectively. Ultimately, the function returns the calculated sum of odd numbers in even positions in the list.