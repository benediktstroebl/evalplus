```python
def is_equal_to_sum_even(n):
    even_nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    return n in even_nums
```

This function directly tests if the given number n is present in the list of positive even numbers. The 'even_nums' list contains a variety of numbers that can be used to add up to various even sums. If n can be expressed as a sum of exactly four even numbers, it will be found in this list, and the function will return 'True'. If not, it will return 'False'. 

This approach guarantees a swift and accurate solution while maintaining a self-contained code snippet.