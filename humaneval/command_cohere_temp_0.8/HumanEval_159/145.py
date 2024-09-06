Here's a Python script that contains a function eat() that solves the given problem:
```python
def eat(n, need, rem):
    return [n + min(need, rem), max(0, rem - need)]
```
This function uses python's expressive min() and max() functions to achieve the desired outcome. It takes in 3 parameters: number of carrots already eaten `n` ; target number of carrots to eat `need` ; and the remaining number of carrots in stock `rem`. The min() function ensures the rabbit eats only the required amount, even if that number is less than the remaining stock. While the max() function handles the case where the rabbit eats its fill, but there isn't enough to satisfy its appetite. 

This solution works for the following example cases:
* eat(5, 6, 10) -> [11, 4]
* eat(4, 8, 9) -> [12, 1]
* eat(1, 10, 10) -> [11, 0]
* eat(2, 11, 5) -> [7, 0]

As the constraint specifies, these values are constrained to be less than or equal to 1000, ensuring the robustness of the function even with large values. 

This solution can be used as a standalone function in Python to solve the given problem.