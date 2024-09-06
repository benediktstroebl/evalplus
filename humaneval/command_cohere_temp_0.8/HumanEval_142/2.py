```python
def sum_squares(lst):
    result = 0
    for i, num in enumerate(lst):
        if i % 3 == 0:
            num **= 2
        elif i % 4 == 0 and i % 3 != 0:
            num **= 3
        result += num
    return result
```

The script introduces a function **sum_squares** that takes a list of integers as input. It undergoes a loop, enumerating each entry in the list. The entries are then squared if their index is a multiple of 3, and cubed if their index is a multiple of 4 and not a multiple of 3. The function subsequently adds up all the modified numbers and returns the sum, effectively solving the problem. 

This approach enables the function to manipulate list entries based on their indices' divisibility, resulting in the desired sum. 

To ensure clarity and readability, it's good practice to include explanations and variable names that convey the purpose of the operations being performed, thereby enhancing the overall code quality.