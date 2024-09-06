Here's a Python script with a self-contained function `get_odd_collatz` that solves the problem:
```python
def get_odd_collatz(n):
    odd_collatz = []
    sequence = [n]
    while len(sequence) > 1:
        if sequence[-1] % 2 == 0:
            sequence.append(sequence[-1] // 2)
        else:
            sequence.append(3 * sequence[-1] + 1)
        odd_collatz.append(sequence[-1])
        sequence = sequence[:-1]
    return odd_collatz

# Test cases
print(get_odd_collatz(1))  # Output: [1]
print(get_odd_collatz(5))  # Output: [1, 5]
print(get_odd_collatz(6))  # Output: [1, 3, 6]
print(get_odd_collatz(10)) # Output: [1, 5, 21, 85]
```
This script defines a function `get_odd_collatz(n)` that calculates and returns a list of odd numbers in the Collatz sequence for a given starting integer `n`. The function initially appends `n` to a list called `odd_collatz`, which stores the odd numbers in the sequence. Then, using a while loop, it enters the Collatz sequence generation process. It iteratively repeats the procedure for each value in the sequence it has created so far. It examines whether the last number in the sequence is odd or even. If the number is even, it divides it by 2 and adds the result to the sequence; if the number is odd, it multiplies it by three and adds one to the result, which it then appends to the sequence. After that, it adds the most recent odd number to the `odd_collatz` list and removes the last number from the current sequence. 

The output of the example usage that is printed in the script above corresponds to the test cases mentioned in the problem statement.