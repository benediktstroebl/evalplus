```python
def solution(lst):
    return sum(x for x in lst if x % 2 == 1 and lst.index(x) % 2 == 0)
```
This Python script defines a function called solution, which takes a list lst as input. It uses a generator expression and the sum function to calculate the sum of odd numbers present in even positions in the list. The index of the list is also used to ensure odd numbers in the list, and the sum is correctly computed for the even positions. The function returns the computed sum of odd numbers in even positions. Overall, the code provides an efficient solution to the problem as stated in the markdown code block.