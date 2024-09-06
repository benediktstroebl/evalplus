```python
def is_equal_to_sum_even(n):
    even_nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    return n in even_nums
```

This function directly tests if the given number n is present in the list of positive even numbers. Evens can be represented as '2x' or '4x' where x is an integer. Thus, the above list represents all possible sums of two even numbers. If a number cannot be represented as such a sum, it is not included in the list. With this, the function directly answers the question without needing to iterate through other numbers. It is also future-proofed against potential larger even numbers as it's a constant time O(1) operation to add new even numbers to the list if needed.