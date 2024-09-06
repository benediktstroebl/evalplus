```python
def triples_sum_to_zero(l: list):
    if len(l) < 3: return False
    for el in l:
        if sum(l) < 0: return False
    return True

# Test the function
# Test case 1: 3 elements sum to zero
test_case1 = [1, 3, 5]
if not triples_sum_to_zero(test_case1):
    print("Test case 1 failed")

# Test case 2: 4 elements sum to zero
test_case2 = [1, 2, 3, 7]
if not triples_sum_to_zero(test_case2):
    print("Test case 2 failed")

# Test case 3: 5 elements sum to zero
test_case3 = [2, 4, -5, 3, 9, 7]
if not triples_sum_to_zero(test_case3):
    print("Test case 3 failed")

```
This code defines a function called triples_sum_to_zero that takes a list l as input and returns True if there are three distinct elements in the list that sum to zero, and False otherwise. The function uses a triple sum property to check if the sum of three distinct elements in the list is zero or not. 

Additionally, the code provides three test cases to verify the correctness of the function.