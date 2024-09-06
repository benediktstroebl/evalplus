```python
def solution(lst):
    return sum(x for x in lst if x % 2 == 1 and lst.index(x) % 2 == 0)
```
This Python script defines a function called solution, which takes a list of numbers as input. This function calculates the sum of all odd numbers present in the even positions of the list. To achieve this, it uses a generator expression, filtering out elements that satisfy the condition of being odd (x % 2 == 1) and appearing in an even index (index() % 2 == 0) in the list. The sum function then adds up these filtered values, returning the result. 

The script tests the function on multiple examples, and the expected output matches the sum of odd elements in even positions for each example provided.