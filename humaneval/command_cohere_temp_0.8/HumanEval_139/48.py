```python
def special_factorial(n):
    factorial_list = [1]
    for i in range(2, n+1):
        factorial_list.append(i * factorial_list[i-1])
    return factorial_list[n]
```
This Python script defines a function `special_factorial` that calculates the 'Brazilian factorial' as defined in the problem statement. The function starts with an initialization of a list, `factorial_list`, with 1 added as the first element. It then iterates through numbers from 2 to `n` (inclusive), where `n` is the input to the function. During each iteration, it calculates the next element in the `factorial_list` by multiplying the current number (`i`) with the factorial of the previous number (`factorial_list[i-1]`). This continues until the length of the `factorial_list` reaches `n`, at which point the value at the top of the list is returned, giving the Brazilian factorial for the input `n`. 

The script ensures that the recursive calculation of factorials is avoided, making it efficient for larger inputs.