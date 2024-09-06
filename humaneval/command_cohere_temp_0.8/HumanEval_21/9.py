Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    return [((x - min(numbers)) / (max(numbers) - min(numbers))) * 1 for x in numbers]
```
The function `rescale_to_unit` takes a list of numbers as input and returns a transformed list where the smallest number is 0 and the largest number is 1. Tests can be run against this function to verify its correctness.  For example:
```python
# test list
input_list = [1.0, 2.0, 3.0, 4.0, 5.0]

# function call
result = rescale_to_unit(input_list)

# print result
print(result)
# [0.0, 0.25, 0.5, 0.75, 1.0]
``` 
This will produce the expected output, as shown in the problem statement. 
This approach provides an efficient solution to the problem with a concise code.  This is achieved by using `list comprehension` to calculate each value in the list by applying the linear transformation to the corresponding element in the original list, assuming the list is sorted.  The `typing` module is used to declare the type of the input parameter for better code readability and to ensure that the function accepts only lists of numbers.  This declaration can help with tooling support and static type checking to catch potential issues or improve the development experience.  Finally, the function returns the transformed list, achieving the desired result of scaling the values between 0 and 1.  This approach maintains the relative relationships and distribution of values in the list.  It is important to ensure that the input list has at least two elements to avoid errors or undefined behavior.  This can be done during the function's validation or by handling edge cases before performing the transformation.  This solution provides a straightforward approach that is easy to understand and apply, making it convenient for manipulating data in scaling transformations.  The `rescale_to_unit` function can be a valuable tool for other scaling operations or analysis tasks that require linearly scaling data to a unit range.  It can be easily adapted to handle other data types, such as integers or other numerical ranges, providing a flexible foundation for data scaling transformations in various contexts.  Great! 
This approach adheres to Python best practices, including the use of a consistent style, descriptive variable names, and type hints to enhance code readability, maintainability, and compatibility with various type-checking tools.  Feel free to inspect this solution and customize it according to your needs.  If you have more questions or would like to discuss other aspects of this solution, feel free to ask!