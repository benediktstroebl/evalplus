```python
def add(x: int, y: int):
    """
    Add two numbers x and y
    Returns:
        int: Sum of x and y
    """
    return x + y
```
The function body consists of a single line that returns the sum of two integers. It fulfills the requirement of adding two numbers and provides a clear explanation of its purpose in the documentation string. This way, the code is both functional and self-explanatory, making it easy for users to understand and use the function. 
If you want to test this function, you can call it with two integer arguments to see the computed sum. 

For example:
```python
add(2, 5)  # Output: 7
```
Or you can include the test blocks directly inside the function, as provided in the original prompt:
```python
def add(x: int, y: int):
    """
    Add two numbers x and y
    Returns:
        int: Sum of x and y
    """
    >>> add(2, 3)
    5
    >>> add(5, 7)
    12
    return x + y
```
This way, when the function is called without any arguments, the test blocks automatically verify the correctness of the function and display the expected output. Giving this scenario, the function would not return any visible output if tested individually, as the assertions would already be executed and cleared from the console. 
However, if you wish to see the output again, you can remove the assertions, and the function will print the sums accordingly. 
Here's the code modified for that option: 
```python
def add(x: int, y: int):
    """
    Add two numbers x and y
    Returns:
        int: Sum of x and y
    """
    print(x + y)
    return x + y
``` 
In this version, when the function is called, it will directly print the sum of the two numbers. 
For example:
```python
add(2, 5)  # Output: 7
``` 
Feel free to choose the version that best suits your needs and testing requirements.