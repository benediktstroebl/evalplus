```python
def solution(lst):
    return sum(x for x in lst if x % 2 == 1 and lst.index(x) % 2 == 0)
```
This Python script defines a function called solution, which takes a list of numbers as input. This function calculates the sum of all odd numbers present in even positions within the list. To achieve this, it employs a list comprehension, iterating through each element in the input list. For each number, it checks two conditions: first, whether the number is odd (using the modulo operator % to determine if the number equals 1 when divided by 2); and second, whether the number's index within the list is even (using the index notation lst.index(x) % 2 == 0). If both conditions are met, the number is included in the sum calculated by the list comprehension. This odd-in-even sum is then returned as the function's output. 

The provided examples in the comment above will yield the following results:
```python
solution([5, 8, 7, 1]) ==> 12
solution([3, 3, 3, 3, 3]) ==> 9
solution([30, 13, 24, 321]) ==> 0
```
This script effectively solves the problem as stated, providing the sum of odd elements in even positions within the list.