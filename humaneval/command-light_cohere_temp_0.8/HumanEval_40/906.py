```python
def triples_sum_to_zero(lst):
    return any(sum(t) == 0 for t in zip(*lst))

# Test suite
tests = {
    "three distinct elements sum to zero" => lambda lst: triples_sum_to_zero(lst) == True
}

if __name__ == "__main__":
    unittest.py.show Discover(unittest.test())

``` 
This script defines a `triples_sum_to_zero` function that checks if there are three distinct elements in a list that sum to zero. It then uses the test suite to test the function. 

This test suite creates a lambda function that creates a list and passes it to the `triples_sum_to_zero` function. The function returns `True` if there are three distinct elements in the list that sum to zero, and `False` otherwise. 
You can add additional test cases to further test the function.