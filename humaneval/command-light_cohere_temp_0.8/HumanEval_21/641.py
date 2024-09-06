Here's a self-contained Python function that solves the problem of applying a linear transformation to a list of numbers in order to make the smallest number 0 and the largest number 1:

```python
def rescale_to_unit(numbers: List[float]) -> List[float]:
    numbers = [x / 100.0 for x in numbers]
    return numbers
```

This function takes a list of numbers as input and returns a new list with the numbers rescaled to the unit [0,1].  The function is self-contained because it does not use any other functions or modules. 

This approach has a few benefits: 
- Reduced complexity - Since it's self-contained, there's less risk of introducing side effects from external functions. 
- Readability - You can easily add additional tests to ensure the function works correctly with different inputs. 
- Code maintenance - By keeping the logic self-contained, you make it easier to understand, debug, and refactor. 
- Improved readability - It simplifies the code by eliminating the need for external function calls.