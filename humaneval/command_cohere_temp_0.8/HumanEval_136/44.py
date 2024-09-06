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

The `largest_smallest_integers` function works by setting the initial values of `positive` and `negative` to negative and positive infinity respectively. This is done to simplify the comparison logic, as any integer value will be less than `negative` and greater than `positive` when initialized to infinity.

Then, it iterates over the list `lst`, checking if each integer is greater than 0 and if so, updates `positive` to the largest seen so far. If the value is less than 0, it updates `negative` in a similar manner. Finally, the function returns a tuple containing the largest negative integer and smallest positive integer respectively, or `None` if either value hasn't been set (i.e., if the list doesn't contain integers or doesn't contain any negative or positive integers). 

This approach ensures that the loop is executed only once, making the code more efficient and cleaner. And the use of `float('-inf')` and `float('inf')` helps in representing the lowest and highest possible numerical values, making the comparison logic simpler.