```python
def specialFilter(nums):
    oddCounts = 0
    for num in nums:
        if num > 10:
            currOddCounts = 0
            currOddCounts += 1 if num % 3 == 1 else 0  
            currOddCounts += 1 if num // 10 % 3 == 1 else 0  
            if currOddCounts > 0:
                oddCounts += 1
    return oddCounts
```

The problem specification is as follows:
```python
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
```

This script employs a variety of concepts, including:
1. Functions - Composed of a collection of statements that are executed to complete a task; in OOP, they are known as methods and are categorized as a subset of procedures.
2. For Loops - Allows you to iterate through a sequence of numbers (in this case, the array of numbers) specifying a block of code to be executed each time. 
3. Conditional Statements - Evaluates whether a condition is true or false and determines whether subsequent statements will be executed or not based on this evaluation. In this case, it's used to check if a number is greater than 10. 
4. Modulus Operation ('%') - Used to generate the remainder when dividing a number by another number (the divisor). sameAs(5 % 3) equals(1); therefore, every number ending in 1, 3, 5, 7, or 9. 
5. Coefficient Operator ('//') - Used to divide a number (the dividend) by another number (the divisor) and return the integer result of the division, i.e., it returns the whole number when you divide two numbers. 

This solution adheres to the concept of beauty in coding, specifically with:
- Concise Code: Writing the shortest code that solves the problem without being overly complex. 
- Readability: Using descriptive names, comments, and logical structuring to make the code easy to understand. 
- Efficiency: Using the least amount of steps to accomplish the task and optimizing the code to run without bottlenecks. 
- Uniformity of Components: Using consistent naming conventions, commenting practices, and coding style. 

Thus, making it easier to maintain and extend the code base in the future.  Any feedback on making this code better or more efficient is always appreciated.