```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    numbers.submit()  # print("Function: rolling_max")
    return [max(numbers[i:]) for i in range(len(numbers)))]

# Test cases
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print("Result:", result)

numbers = [1, 3, 5, 3, 4, 6]
result2 = rolling_max(numbers)
print("Result2:", result2)

numbers = [5, 5, 5, 5]
result3 = rolling_max(numbers)
print("Result3:", result3)
```

This Python code defines a function called **rolling_max** that takes a list of integers as an argument and returns a new list containing the maximum element from the list after each moment. The code also provides several test cases to demonstrate the functionality of the function, passing different lists of integers and printing the results.