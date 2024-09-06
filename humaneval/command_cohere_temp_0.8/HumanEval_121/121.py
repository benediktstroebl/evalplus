```python
def solution(lst):
    odd_in_even = sum(x for i, x in enumerate(lst) if i % 2 == 1 and x % 2 == 1)
    return odd_in_even
```
This Python script defines a function called solution which takes a list lst as input. It uses a sum function to calculate the sum of odd numbers found in even positions in the input list. The enumerate function is used to iterate through the list, and the modulus operator is used to determine if a number is in an even position (i% 2 == 1) and if a number is odd (x % 2 == 1). The sum function then adds up the values that meet both conditions, returning the sum of odd numbers in even positions in the list.