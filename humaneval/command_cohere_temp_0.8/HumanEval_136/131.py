```python
def largest_smallest_integers(lst):
    positive = float('-inf')
    negative = float('inf')
    for n in lst:
        if n > 0 and (n < positive or positive == float('-inf')):
            positive = n
        if n < 0 and (n > negative or negative == float('inf')):
            negative = n
    return (negative if negative != float('inf') else None,
            positive if positive != float('-inf') else None)
```

The `largest_smallest_integers` function iterates through the list, tracking the largest positive and smallest negative integers encountered. Using `float('-inf')` and `float('inf')` allows for efficient recognition of the most extreme values. If no negative or positive integer is found, `None` is returned for either part of the tuple.

This approach ensures that the function correctly identifies the desired values while handling all edge cases mentioned in the problem statement. Let's break down the code step by step:
1. **Function Definition**:
   ```python
   def largest_smallest_integers(lst):
       ...
   ```
   This code defines a new function named `largest_smallest_integers`, which takes one argument, `lst`, a list of integers.
2. **Initialization**:
   ```python
   positive = float('-inf')
   negative = float('inf')
   ```
   Before beginning the iteration, we initialize two variables, `positive` and `negative`, to special float values, `float('-inf')` and `float('inf')`, respectively. These values represent the lowest possible positive number and the highest possible negative number in Python's floating-point representation.
3. **Iteration**:
   ```python
   for n in lst:
       ...
   ```
   This loop iterates through each integer in the input list.
4. **Updating Extreme Values**:
   ```python
   if n > 0 and (n < positive or positive == float('-inf')):
       positive = n
   ```
   This block checks if the current integer `n` is positive and if it's smaller than the current `positive` value or if `positive` is equal to `float('-inf')` (initially the lowest possible value). If either of these conditions is true, it updates `positive` to the value of `n`, ensuring that `positive` always holds the largest positive integer encountered.

   ```python
   if n < 0 and (n > negative or negative == float('inf')):
       negative = n
   ```
   Similarly, this block checks if the current integer `n` is negative and if it's larger than the current `negative` value or if `negative` is equal to `float('inf')` (initially the highest possible value). If either of these conditions is true, it updates `negative` to the value of `n`, ensuring that `negative` always holds the smallest negative integer encountered.

5. **Return Result**:
   ```python
   return (negative if negative != float('inf') else None,
          positive if positive != float('-inf') else None)
   ```
   Finally, the function returns a tuple containing the largest negative integer (or `None` if none was found) and the smallest positive integer (or `None` if none was found). It uses conditional expressions to determine whether to return the calculated values or `None` in cases where no positive or negative integer was found.

This function ensures the correct solution is obtained regardless of the order of integers in the list and handles cases where the list might be empty or contain only zeros.