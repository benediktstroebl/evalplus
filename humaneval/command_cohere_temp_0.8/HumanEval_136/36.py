```python
def largest_smallest_integers(lst):
    positive = None
    negative = None
    for n in lst:
        if n > 0:
            if positive is None or n > positive:
                positive = n
        elif n < 0:
            if negative is None or n < negative:
                negative = n
    return (negative, positive)
```

The script provides a function that handles the task as described in the problem statement and is tested on the examples provided there. 

Let's break down the code step by step:
1. `positive = None` and `negative = None` initially set both variables to `None`, preparing them to be updated later in the loop.
2. The `for` loop iterates through every integer in the input list.
3. Inside the loop, there are two conditional checks:
   - If the current integer is greater than zero (`n > 0`), it means there is a positive integer in the list. The `positive` variable is updated if necessary.
   - If the current integer is less than zero (`n < 0`), it means there is a negative integer in the list. The `negative` variable is updated if necessary.
4. The update of `positive` and `negative` is done using the ternary operator for short circuiting (the condition is checked, and the assignment is done only if the condition is met). The line `positive = n` or `negative = n` means that if the `positive` (or `negative`) variable was `None` before, or if the current integer is greater than the previous value of `positive` (or `negative`), the variable is updated to the current integer.
5. After iterating through all integers in the list, the function returns a tuple containing the computed `negative` and `positive`.

The script should provide a solution that follows the spec and returns the correct values for the given test cases.