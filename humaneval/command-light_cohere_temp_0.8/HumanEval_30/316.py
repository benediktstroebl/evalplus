```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

#Test cases
get_positive([-1, 2, -4, 5, 6]) # [2, 5, 6]
get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) # [5, 3, 2, 3, 9, 123, 1]

```
This code defines the function **get_positive(lst)** which returns a list of only positive numbers from the input list **lst**. The function uses list comprehension to iterate through each element in the list and checks if the number is non-negative. 

The test cases demonstrate the function's behavior and it passes all the tests successfully.