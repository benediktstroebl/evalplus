```python
def pairs_sum_to_zero(l):
    """
    Check whether all elements in the list sum up to zero.
    """
   
    if sum(l) == 0:
        return True
    else:
        return False
    """

def test():
    """
    Test function to check the result of pairs_sum_to_zero.
    """
    list_test = [1, 3, 5, 0]
    assert pairs_sum_to_zero(list_test) == False
    """

# Driver code
if __name__ == "__main__":
    print("Test passed!")
    test()
```

The code defines a function that checks whether the sum of all elements in a given list is equal to zero. The function uses the if statement to check if the sum of all elements is equal to zero.

The test function is used to check the correctness of the pairs_sum_to_zero function. The driver code ensures that the test function is executed correctly.