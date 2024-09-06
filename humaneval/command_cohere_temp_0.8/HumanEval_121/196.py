```python
def solution(lst):
    odd_in_even = sum(x for x in lst if x % 2 and lst.index(x) % 2 == 0)
    return odd_in_even
```
This Python script provides a function called solution(), which takes a list of integers as input and returns the sum of all odd numbers present at even positions within the list. To do this, it employs a list comprehension, iterating through each element x in the input list lst. For each element, it checks two conditions: first, whether the element x is odd using the modulus operator % 2, and second, whether its index in the list lst is even, which is checked using the modulo operation lst.index(x) % 2 == 0. If both conditions are true, the value of element x is added to the running sum with the sum() function. Finally, the function returns the computed sum of odd numbers in even positions.