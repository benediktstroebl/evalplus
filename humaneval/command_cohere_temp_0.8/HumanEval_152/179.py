```python
def compare(game, guess):
    return [abs(x-y) if x != y else 0 for x, y in zip(game, guess)]
```
This function takes two equal-length lists, game and guess, as arguments. It returns a list of the same length, comparing each element in the two lists, calculating the absolute difference between the two elements if they don't match, and returning 0 if the elements match. This result is then returned as a list.

The overall time complexity of this function is `O(n)` where `n` represents the number of elements in the two lists. This is because the function iterates through each element in both lists just once, performing basic operations on each element.

This solution should be able to efficiently process large datasets due to its linear time complexity and minimal computational overhead. 

Note: This solution assumes that the two lists have the same length, and performs unpredictably if this precondition is not met. It is always good practice to ensure assumptions like this are clearly communicated, and ideally, checked for in the code.