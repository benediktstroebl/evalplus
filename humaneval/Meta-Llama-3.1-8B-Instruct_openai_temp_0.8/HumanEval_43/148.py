### Pairs Summing to Zero
#### Problem Description
Given a list of integers, determine if there are two distinct elements that sum to zero.

#### Solution
```python
def pairs_sum_to_zero(lst):
    """
    Returns True if there are two distinct elements in the list that sum to zero, and False otherwise.
    
    Args:
    lst (list): A list of integers.
    
    Returns:
    bool: Whether two distinct elements in the list sum to zero.
    """
    seen = set()  # Initialize a set to store seen numbers
    for num in lst:
        complement = -num  # Calculate the complement of current number
        if complement in seen:  # Check if complement is seen before
            return True  # Two distinct elements sum to zero
        seen.add(num)  # Add current number to seen set
    return False  # No pairs found that sum to zero

# Example use cases
if __name__ == "__main__":
    test_cases = [
        [1, 3, 5, 0],
        [1, 3, -2, 1],
        [1, 2, 3, 7],
        [2, 4, -5, 3, 5, 7],
        [1]
    ]
    
    for case in test_cases:
        print(f"Input: {case}, Output: {pairs_sum_to_zero(case)}")
```
In this solution, we use a set `seen` to keep track of the numbers we have seen so far. For each number in the input list, we calculate its complement (-num) and check if it is in the `seen` set. If it is, we return True, indicating that two distinct elements sum to zero. Otherwise, we add the current number to the `seen` set and continue to the next number. If we finish iterating through the list without finding any pairs that sum to zero, we return False.