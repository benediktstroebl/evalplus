```python
def will_it_fly(q, w):
    return (sum(q) <= w) and check_palindrome(q)

def check_palindrome(q):
    return q == q[::-1]

# Test cases
q1 = [1, 2]
w1 = 5
print(will_it_fly(q1, w1)) # Expected output: False

q2 = [3, 2, 3]
w2 = 1
print(will_it_fly(q2, w2)) # Expected output: False

q3 = [3, 2, 3]
w3 = 9
print(will_it_fly(q3, w3)) # Expected output: True

q4 = [3]
w4 = 5
print(will_it_fly(q4, w4)) # Expected output: True
``` 

The function `will_it_fly` returns True if the object `q` will fly, and False otherwise. The object `q` will fly if it is both balanced and the sum of its elements is less than or equal to the maximum possible weight `w`. The balanced state is checked by the function `check_palindrome` which confirms if the list is a palindrome.

The test cases verify the function for different scenarios and the expected results are printed accordingly. You can modify or add more test scenarios to thoroughly test the function.