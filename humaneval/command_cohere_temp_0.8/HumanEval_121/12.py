```python
def solution(lst):
    return sum(num for ind, num in enumerate(lst) if ind % 2 == 1 and num % 2 == 1)
```
This Python script defines a function called solution, which takes a list of integers as input. It employs a sum function iteration through the list, checking if the current element is odd and it is positioned in an even index. The result is the sum of odd elements in even positions. The function returns the sum. Overall, this solution is concise and straightforward.