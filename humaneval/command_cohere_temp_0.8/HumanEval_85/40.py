```python
def add(lst):
    even_odd = [el for i, el in enumerate(lst) if i % 2 == 1 and el % 2 == 0]
    return sum(even_odd)
```
This Python script defines a function named 'add', which takes a list of integers as input. It aims to accumulate and return the sum of even integers present at odd indices in the input list. To achieve this, the function employs a list comprehension, which iterates through each element and index of the input list. If the current index is odd and the corresponding element is even, it adds the element to the 'even_odd' list. Finally, the function returns the sum of the elements in 'even_odd,' resulting in the desired sum of even integers at odd indices in the input list. 

Here is a test drive code snippet that showcases the functionality of the function: 
```python
test_list = [4, 2, 6, 7]
print(add(test_list))  # Output: 2 (4 + 6)
``` 
This demonstrates the function's ability to identify even elements at odd indices (2 and 6) and compute their sum, resulting in the output 2.