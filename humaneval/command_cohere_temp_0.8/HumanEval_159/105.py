Here's a Python script that contains a function eat() that solves the problem described in the code block above:
```python
def eat(n, need, remaining):
    if remaining >= need:
        total = n + need
        return [total, remaining - need]
    else:
        total = n + remaining
        return [total, 0]

# Example usage
print(eat(5, 6, 10))  # Output: [11, 4]
print(eat(4, 8, 9))  # Output: [12, 1]
print(eat(1, 10, 10))  # Output: [11, 0]
print(eat(2, 11, 5))  # Output: [7, 0]
```

This script includes the `eat()` function that takes three integer parameters, `n` (number of carrots already eaten), `need` (number of carrots needed to eat), and `remaining` (number of remaining carrots in stock). The function calculates the total number of carrots eaten and the remaining carrots after eating.

The example usage demonstrates how to call the `eat()` function with different input values and print the returned results, matching the expected output as stated in the prompt.

This solution adheres to the specified constraints and provides an efficient way to manage the rabbit's carrot eating and remaining quantity. 

I hope this solves your problem, let me know if you need anything else!