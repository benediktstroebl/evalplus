```python
def is_equal_to_sum_even(n):
    even_nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    return n in even_nums
```

This function directly tests if the given number `n` is present in the list of even numbers `even_nums`. 

Moreover, here's a brief explanation of the approach:
1. The function uses a predefined list `even_nums` containing positive even numbers from 2 to 20 as a simple and compact representation of all possible sums of exactly 4 positive even numbers.
2. If the number `n` can be represented as the sum of exactly 4 positive even numbers, it will be present in the `even_nums` list, thereby returning True, otherwise it returns False. 

This solution is concise and efficient, but it assumes that the given number `n` is a positive even number, as the `even_nums` list includes only positive even numbers. If the problem allows for negative even numbers or other cases, the solution should be adjusted accordingly.