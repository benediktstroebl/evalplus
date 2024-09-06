```python
def add(lst):
    even_odd = [el for i, el in enumerate(lst) if i % 2 == 1 and el % 2 == 0]
    return sum(even_odd)
```
This Python script defines a function called 'add()'. This function takes a list as input and aims to calculate the sum of even integers present at odd indices in the list. To achieve this, it employs a list comprehension, iterating through each element of the input list. If the current index is odd and the element is even, it adds the element to the 'even_odd' list. Finally, the function returns the sum of the elements in 'even_odd', providing a total for the odd-indexed even integers in the input list. 

The function effectively solves the problem statement and provides a straightforward way to obtain the sum of even integers at odd indices in a given list. 

The script also includes some tests in the comments that can be added to ensure the function performs as expected. 
```python
# Test the function with a sample input
sample_input = [4, 2, 6, 7]
sample_result = add(sample_input)
print(f'For the list {sample_input}, the function adds the even elements at odd indices, resulting in: {sample_result}')

# Test the function with a more complex input
more_complex_input = [2, 5, 6, 8, 1, 9, 4, 7, 3, 10]
complex_result = add(more_complex_input)
print(f'For the list {more_complex_input}, the function adds the even elements at odd indices, resulting in: {complex_result}')
``` 
These tests can be uncommented and executed to validate the function's behavior with different inputs.