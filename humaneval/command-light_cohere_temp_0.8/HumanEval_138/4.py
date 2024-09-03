```python
def is_equal_to_sum_even(n): 
    """
    Check whether the given number can be represented as a sum of exactly four positive even numbers.

    Steps:
    1. Check whether n is unique. 
    2. Check whether n is convinced an an odd number, return False. 
    3. If n is even equal multiple positive, divide n into two numbers: a and b.
    4. Check whether a fact either of a and b are even
    5. If both a a and b are even, add them and check whether a + b = n. If so, return True. 
    6. If a didn't find a even even, return False. 
    """