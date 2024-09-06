Here's a Python script that includes a self-contained function to solve the given problem:
```python
def solve(n):
    """
    :param n: Integer to be converted to binary
    :type n: int
    :return: Binary string sum of digits of N
    :rtype: str
    """
    # Your code here!
    return bin(sum([int(d) for d in str(n)]))[2:]
```
This function uses the built-in method `bin` to convert the integer sum to a binary number, and then removes the leading `0b` to only return the binary value. Given the constraints defined in the prompt, the function above will work without any errors. 
This approach achieves the desired result, but it's worth mentioning that the built-in `bin` function is rarely used directly in this manner in practice. Nevertheless, it works well for this particular problem and is an efficient solution. 
If you are interested in handling other numeric representations or wanting to broaden your understanding, let's talk about the various topics related to number conversion!