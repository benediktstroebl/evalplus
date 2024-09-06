```python
def solution(lst):
    return sum(num for num in lst if num % 2 == 1 and lst.index(num) % 2 == 0)
```
This Python script defines a function called solution, which takes a list of numbers as input. This function calculates the sum of all odd numbers present in even positions within the list. To achieve this, it employs a list comprehension, iterating through each element in the input list. For each number, it checks if the number is odd and whether its index is even (occurring at an even position). If both conditions are met, the number is added to the running sum, returned finally. The function's ability to pinpoint odd numbers in even positions is facilitated by the lst.index() function, which helps determine the even positions of odd numbers within the list. 

This solution adheres to the problem's specified examples, returning the correct sums for the provided input lists.