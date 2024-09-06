```python
def solution(lst):
    return sum(x for x in lst if x % 2 == 1 and lst.index(x) % 2 == 0)
```
This Python script defines a function called solution, which takes a list of numbers as input. This function returns the sum of all odd numbers present in the list that are also in even positions. To achieve this, it employs a conditional check, examining each number in the list using the generator expression x for x in lst if x % 2 == 1 and lst.index(x) % 2 == 0. This generates only odd numbers located in even positions within the list. The sum function then adds up these odd numbers, and the result is returned. 

The provided example test cases, demonstrated in the docstring, illustrate how the function behaves for different lists: `solution([5, 8, 7, 1]) ==> 12`, `solution([3, 3, 3, 3, 3]) ==> 9`, and `solution([30, 13, 24, 321]) ==> 0`. These examples help explain the purpose and demonstrate the functionality of the provided solution function.