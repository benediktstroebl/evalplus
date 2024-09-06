```python
def tri(n):
    result = [0, 1, 3]
    while len(result) < n + 1:
        if len(result) % 2 == 0:
            result.append(1 + result[-1] / 2)
        else:
            x = result[-1]
            y = result[-2]
            z = result[-3]
            result.append(x + y + z)
    return result[:n+1]
``` 

This script defines a function called `tri` that takes a parameter `n`, representing the number of terms to generate for the Tribonacci sequence. To capture the logic of the Tribonacci sequence, the function starts with an initial list of the first three terms [0, 1, 3], then iteratively calculates the next terms based on the recurrence relation.

For each iteration, the function checks if the length of the result list is even or odd to decide whether to use the recurrence for even-indexed terms or odd-indexed terms. 

The generated list is returned, trimmed to the specified length `n+1`. 

This code adheres to the problem statement, providing a self-contained Python function to generate the Tribonacci sequence up to any given term `n`. 

This code can be tested against the provided tests in the markdown code block above.