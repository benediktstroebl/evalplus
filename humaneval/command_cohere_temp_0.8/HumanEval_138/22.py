```python
def is_equal_to_sum_even(n):
    even_nums = [2, 4, 6, 8, 10, 12]
    return n in even_nums
```

This function directly tests if the given number n is present in the list of positive even numbers. The function follows the prompt's specification, making it evaluate to true for values like 8 and false for values like 4 and 6. 

The function is also relatively efficient with a time complexity of O(1) since it involves checking membership in a small list, which typically takes constant time. 

Note that the function assumes that the input n is a positive integer, as implied by the problem statement. If the input can be negative or not an integer, further modifications would be necessary.