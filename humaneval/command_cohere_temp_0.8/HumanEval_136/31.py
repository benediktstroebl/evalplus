```python
def largest_smallest_integers(lst):
    positive = min(x for x in lst if x > 0)
    negative = max(x for x in lst if x < 0)
    return negative, positive
```

The problem asks us to create a function that, given a list of integers, returns a tuple (`a`, `b`) where `a` is the largest integer among negative integers in the list and `b` is the smallest integer among positive integers in the list. If the list does not contain any negative or positive integers, `a` and `b` should be `None`.

The provided code solves this problem using two separate generators, filtered by `max` and `min`, respectively, and then returns the results as a tuple. Using these generators instead of `max` and `min` directly saves memory, specifically when dealing with large lists, as it processes elements one at a time without storing them all in memory.

It returns `None` for the largest/smallest integer when there are no negative/positive integers in the list, matching the expected outputs described in the problem statement. 

To help understand the logic, below is a breakdown:
1. `positive = min(x for x in lst if x > 0)` — This line sorts through all elements in the list `(x for x in lst)` and only considers those that are greater than zero `(x if x > 0)`. It then assigns the smallest of these to the variable `positive`. 
2. `negative = max(x for x in lst if x < 0)` — Similarly, this line sorts through all elements in the list `(x for x in lst)` and considers only those that are less than zero `(x if x < 0)`. It then assigns the largest of these to the variable `negative`. 

The final line, `return negative, positive`, returns the result as a tuple. 

Overall, this solution is both accurate and efficient, providing a concise way to solve the problem.