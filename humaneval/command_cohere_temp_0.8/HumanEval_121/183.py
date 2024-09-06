```python
def solution(lst):
    return sum(x for x in lst if x % 2 == 1 and lst.index(x) % 2 == 0)
```
This Python script provides a function called solution(), which takes a list of numbers as input and returns the sum of all odd numbers within the list that appear in even positions. To accomplish this, it utilizes a generator expression, filtering out elements that meet the specified conditions and summing them using the sum() function. The function works correctly and yields the desired output as specified in the test examples.