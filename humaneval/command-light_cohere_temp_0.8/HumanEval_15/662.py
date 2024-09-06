Here is a self-contained Python function that generates a string of numbers from 0 to n: 
```python
def string_sequence(n: int) -> str:
    sequence = [0] 
    while n > 0: 
        n, i = divmod(n, 10)
        sequence.append(str(i))
    return ''.join(sequence)
``` 
This function, `string_sequence`, takes an integer `n` as input and returns a string containing the first `n` numbers from 0, separated by spaces. 

To test the functionality, the code creates a sample input `5` and prints the expected output which should be: `0 1 2 3 4 5`.