```python
def sort_third(l: list):
    l_copy = l.copy()
    sorted_l = []
    for i in range(len(l)):
        if i % 3 == 0:
            sorted_l.append(sorted(l_copy[i]))
        else:
            sorted_l.append(l_copy[i])
    return sorted_l
```
This Python script defines a function called `sort_third`. This function takes a list `l` as input and returns a new list `l_copy`. The new list is identical to the input list in indices that are not divisible by three, while in the other cases, the values at the indices that are divisible by three are equal to the values of the corresponding indices of `l`, but sorted. This behavior is accomplished by the following steps:
1. Creating a copy of the input list `l` to keep the original values unchanged.
2. Using a list comprehension that takes each index in the `l` list one at a time and checks if the index is divisible by three, by using the modulo operator `%`. If it is divisible by three, it uses the built-in Python `sorted` function to sort the values in the corresponding index of the `l_copy` list and append the result to the `sorted_l` list. If it is not divisible by three, it simply appends the value at the corresponding index in the `l_copy` list. 

While the given description in the markdown code block provides examples that satisfy the problem statement, it does not provide a clear indication of how the function sorts the values at the divisible indices by three, leading to confusion. It seems that testing the function with edge cases and providing clearer documentation on how the function performs the task would be beneficial for users who might use this function in the future.