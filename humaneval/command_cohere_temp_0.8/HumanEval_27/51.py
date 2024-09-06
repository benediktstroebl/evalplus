```python
def flip_case(string: str) -> str:
    return ''.join(char.swapcase() for char in string)
```
This script defines a function `flip_case` that takes a string as an argument and returns a new string with the case of each character swapped. In this case, uppercase characters in the input string will become lowercase in the returned string, and vice versa. 

This solution adheres to the problem statement, as it reflects the desired character flipping behavior, and the function works in isolation, making it self-contained. 

To verify the functionality, you can run this script, which will output the result of the function when called with this input:
```python
print(flip_case('Hello')) 
```
Doing so will print `hELLO` onto the console, confirming the successful execution of the function with the desired case flip.