```python
def solution(lst):
    odd_in_even = sum(x for x in lst if x % 2 and lst.index(x) % 2 == 0)
    return odd_in_even
```
This Python script defines a function called solution which takes a list lst as input. It aims to calculate the sum of odd numbers present in even positions within the list. To achieve this, it employs a list comprehension, iterating through each element x in the input list lst. For each element, it checks two conditions: first, whether the element x is odd (i.e., its remainder when divided by 2 is equal to 1), and second, whether its index in the list lst is even (i.e., the modulus of its index by 2 is equal to 0). When both conditions are satisfied, the value of the element x is added to the running sum odd_in_even. Finally, the function returns the calculated sum of odd numbers appearing in even positions within the list.