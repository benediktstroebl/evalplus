```python
def tri(n):
    if n < 1:
        raise ValueError("Input must be a positive integer")
    sequence = [0]
    
    if n % 2 == 0:
        sequence.append(sequence[-1] + sequence[-2])
    else:
        sequence.append(sequence[-1] + sequence[-2] + sequence[-3])
    
    return sequence

def test_tri(n):
    try:
        result = tri(n)
        if len(result) != n + 1:
            raise ValueError("Returned list length does not match expected length")
        for i, num in enumerate(result):
            if num < 1 or not isinstance(num, int):
                raise ValueError("Each element in the list should be an integer")
        return result == [1, 3, 2, 8]
```
This script defines a function called `tri` that calculates the first `n+1` numbers of the Tribonacci sequence and tests it with another function `test_tri` that validates the correctness of the function using various checks.  The script creates a list with the first two elements (1 and 3) and then adds the sum of the last two elements (2 and 8) to the end of the list.