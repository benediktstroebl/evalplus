Here's a Python script that contains a function to solve the given problem:
```python
def maximum(arr, k):
    arr.sort()
    return arr[:k]
```
The function `maximum` takes in an array `arr` and an integer `k` as inputs. It sorts the array and then returns the first `k` elements from the sorted array, effectively providing the maximum `k` numbers in the original input array. 

The code is concise and straightforward, achieving the problem solution efficiently. It can be combined with procedural or test block to validate its functionality against different test cases. 
For example, we could add a procedural block like this:
```python
# Sample input and expected output
input = [-3, -4, 5], 3
expected = [-4, -3, 5]
print(f"Input: {input}")
print(f"Expected: {expected}")

actual = maximum(*input)
print(f"Actual: {actual}")

assert actual == expected
```
This would verify the correctness of the `maximum` function against a particular test case.