```python
def sum_to_n(n):
    """Returns the sum of the first n integers.
    
    Args:
        n (int): Summates integers up to this value.
        
    Returns:
        int: Sum of integers from 1 to n.
    """
    return n * (n + 1) // 2  # Sum of integers from 1 to n is n(n+1)/2

# Testing the function
# To run tests uncomment the following block
# and execute the script
# >>> sum_to_n(30)
# 465
# >>> sum_to_n(100)
# 5050
# >>> sum_to_n(5)
# 15
# >>> sum_to_n(10)
# 55
# >>> sum_to_n(1)
# 1
```

This function definition takes an integer `n` as input and returns the sum of the first `n` integers. The function utilizes a closed form summation formula where the sum of integers from 1 to n is equal to `n * (n + 1) // 2`. 

The block of test cases is included to validate the function's behavior and ensure it behaves as expected for various inputs. You can uncomment these test cases and execute the script to verify the function's correctness. 

I have added comments to explain the purpose of each part of the code including the argument and return value definitions, as well as the testing mechanism. 
If you have any questions, let me know!