```python
def string_sequence(n: int) -> str:
    """ 
    Return a string containing space-delimited numbers starting from 0 upto n inclusive. 
    """ 
    if n <= 0: 
        return 'Invalid Input'
    """
    if n <= 0: 
        return 'Invalid Input'
    return " ".join(str(i) for i in range(n))

# test case 1: Test string sequence function with an invalid input (negative number)
assertEqual(string_sequence(-5),'Invalid Input')

# test case 2: Test string sequence function with a valid input (positive number)
assertEqual(string_sequence(5),'0 1 2 3 4 5')
```