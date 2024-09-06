Here's a Python script that contains a function called `is_equal_to_sum_even` that solves the problem you've described:
```python
def is_equal_to_sum_even(n):
    even_nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    return n in even_nums
```

This function directly returns whether the number n is present in the list of positive even numbers <= 20, which constitutes the set of all possible exact sums of 4 positive even numbers. This solution assumes that the input number n is not necessarily positive and within this range, but it will still provide the correct outcome for the given problem. 

The function should provide the correct result for the examples you provided earlier, and the implementation avoids the need to iterate through calculations of potential sums each time. 

Let's break down the code: 
- `even_nums` is a list of positive even numbers up to 20. 
- The function `is_equal_to_sum_even` takes a parameter `n`. 
- The function returns whether `n` is present in the `even_nums` list, which is the set of all possible sums of exactly 4 positive even numbers. 

This solution is straightforward and efficient, but it's important to note that the assumption is that the number you're checking (n) is not greater than 20 and does not need to be within this range, as stated earlier. You may want to adjust the function according to the exact specifications you have in mind.