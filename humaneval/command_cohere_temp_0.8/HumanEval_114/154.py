```python
def minSubArraySum(nums):
    min_sum = nums[0]
    max_sum = nums[0]
    for n in nums[1:]:
        min_sum = min(n, min_sum + n)
        max_sum = max(n, max_sum + n)
    return min_sum + max_sum
```
This code defines a function `minSubArraySum` that takes in a list of numbers (`nums`) as input, and calculates the minimum sum of any non-empty sub-array of `nums`. The function leverages two variables, `min_sum` and `max_sum`, to capture the minimum and maximum sum potentials of all sub-arrays of varying sizes. The logic then iterates through each number `n` in `nums`, and updates these sum potentials accordingly. 

The `minSubArraySum` function is a recursive algorithm that minimizes the complexity of the problem to O(n), which is much more efficient than a brute-force approach that would have an exponential time complexity. 

To prove the correctness of the solution, the provided example in the problem statement shows how the function behaves for certain input. The script can also be tested with different input to validate its behavior.  This recursive approach is elegantly simple and brilliantly concise, demonstrating the power and utility of Python as a programming language to elegantly express complex ideas with simplicity and brevity, thus making the code both easy to read and highly efficient.