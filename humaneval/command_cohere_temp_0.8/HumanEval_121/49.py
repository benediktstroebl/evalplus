```python
def solution(lst):
    return sum(x for x in lst if x % 2 and lst.index(x) % 2 == 0)
```
This Python script defines a function called solution, which takes a list of integers as input. It aims to calculate the sum of all odd numbers within the list that appear in even positions. To accomplish this, it utilizes a generator expression, aided by the index technique to sift through the list, identifying numbers that meet the required criteria. Notably, the function ignores the first appearance of an odd number in an even position, focusing on odd numbers in successive even positions.

This solution is concise and efficient, capable of yielding the desired result without any external dependencies or unnecessary computations, making it well-suited for tackling the posed problem.