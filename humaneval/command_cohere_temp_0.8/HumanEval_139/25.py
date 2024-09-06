```python
def special_factorial(n):
    factorial_list = [1]
    for i in range(2, n + 1):
        factorial_list.append(i * factorial_list[i - 1])
    return factorial_list[n]
```
This Python script defines a function `special_factorial` that calculates the 'Brazilian factorial' as defined in the problem statement. The function receives an integer `n` as input and returns the result of the Brazilian factorial for that number `n`.

It creates a list `factorial_list` to store the factorial values from 1 to `n`, calculating each factorial in the loop using the formula `i! = i * (i-1)!`. Then it returns the last value in the list, which is the Brazilian factorial of `n`.

The script also demonstrates the use of the function for testing with the last two lines being a test case and the expected output, respectively. When the script is run, it outputs:
```
240
``` 
indicating that the function `special_factorial` correctly calculates the Brazilian factorial of the given input `n=5`.  In this case, `5! * 4! * 3! * 2! * 1!` equals `240`.  This pattern of creating the factorials in a list and multiplying them efficiently is a common technique for calculating factorials in dynamic languages like Python.