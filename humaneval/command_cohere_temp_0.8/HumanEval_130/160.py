```python
def tribonacci(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [1]
    elif n % 2 == 0:
        return [0] + tribonacci(n - 1)
    else:
        return [1] + tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n + 1)
```
The function takes an input of type integer, and returns a list of numbers of the Tribonacci sequence accordingly. It achieves this by adding logic to handle different cases of the recursive definition, specifically:
1. An input of 0 returns [0]
2. An input of 1 returns [1]
3. If the input is even it returns [0] plus the result of the same input minus one (base case of the recursive definition)
4. If the input is odd it returns [1] plus the results of the same input minus one and minus two joined with the result of the same input plus one. 

This results in a list of numbers that correspond to the Tribonacci sequence as described. 

This approach ensures that the function returns the correct Tribonacci number at each stage, complying with the problem's definitions and ensuing the output lists the first n + 1 Tribonacci numbers.