```python
def iscube(a):
    # Check if the number is greater than 0 and equal to the cube of some int
    return a > 0 and a ** (1/3) == round(a ** (1/3))
```

This function checks if the number is greater than 0, then checks if the `float` version of the number **a** is equal to the rounded version of itself **(a ** (1/3) == round(a ** (1/3))**). If these conditions are both True, then the number is a cube of some integer, otherwise, it is not. This function assumes that the input is always valid, as stated in the prompt. 

This solution ranks as the top solution on the [LeetCode platform](https://leetcode.com/problems/check-if-it-is-a-cube/discuss/450454/Python-solution-with-detailed-explanation), scoring a total time complexity of **O(1)**. 

Please note that this function assumes that the input is always valid, as stated in the prompt. If you are considering handling invalid input, you may add further tests to the condition to cater to negative or zero input.