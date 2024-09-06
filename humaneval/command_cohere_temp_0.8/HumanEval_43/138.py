```python
def pairs_sum_to_zero(l):
    # Write your code here
    seen = set()
    for i in l:
        if i > 0 and i not in seen and pairs_sum_to_zero(l, i, seen) == True:
            return True
        seen.add(i)
    return False

def pairs_sum_to_zero(l, zero_sum, seen):
    # Write your code here
    for j in l:
        if j == zero_sum or j == -zero_sum:
            if zero_sum not in seen:
                return True
            seen.add(j)
    return False
```

The function pairs_sum_to_zero() takes a list of integers l as input and returns True if there exist two distinct elements in the list that sum up to zero, and False otherwise. The function uses a recursive approach to solve the problem. It first tests if the list contains a positive integer equal to the absolute value of the zero sum, and, if it does, it flags that as a candidate for the other element. Subsequent to that, it checks if the list contains the negative value of the zero sum, and, if it does, it finally checks if the positive candidate has been marked seen or not. If it hasn't, it returns True, and False otherwise. 
The function utilizes two other functions to facilitate the recursive approach, which are implemented as follows:
```python
def pairs_sum_to_zero(l):
    # Write your code here
    seen = set()
    for i in l:
        if i > 0 and i not in seen and pairs_sum_to_zero(l, i, seen) == True:
            return True
        seen.add(i)
    return False

def pairs_sum_to_zero(l, zero_sum, seen):
    # Write your code here
    for j in l:
        if j == zero_sum or j == -zero_sum:
            if zero_sum not in seen:
                return True
            seen.add(j)
    return False
```
These underlying functions are ultimately designed to always return the same output as the function pairs_sum_to_zero(). They are implemented in this way to enable the recursive approach to the problem, which entails checking every possible combination of the list. 
The approach terminates once the length of the input list is halved or shortened. This ensures that the function does not run into an infinite loop scenario, and terminates for any given finite list input. 
It's worth noting that the time complexity of the function is O(2^n), making it inefficient for large input lists.