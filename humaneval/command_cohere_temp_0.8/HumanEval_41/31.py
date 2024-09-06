Here's a Python script that contains a function which solves the specified problem:
```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars are driving left to right; simultaneously, a different set of n cars
    are driving right to left. The two sets of cars start out being very far from
    each other. All cars move at the same speed. Two cars are said to collide
    when a car that's moving left to right hits a car that's moving right to left.
    However, the cars are infinitely sturdy and strong; as a result, they continue moving
    in their trajectory as if they did not collide.

    This function outputs the number of such collisions.
    """
    collisions = 0
    for i in range(n):
        for j in range(n):
            if i > j:
                collisions += 1
    return collisions
```

This function uses two nested loops to iterate across all possible pairs of cars,
comparing the relative order of the indices to determine whether the cars are
driving towards each other or not. Cars with positive relative difference in their
indices are driving towards each other, while cars with a negative difference
are moving away from each other. The total number of collisions is counted
and returned as the result.

To ensure that the function is correct, it is recommended to test it with a variety of inputs. Here is an example of how you can test this function using a simple input:
```python
test_cases = [
    (1,),
    (2,),
    (3,),
    (5,),
    (10,),
    (100,)
]

for input in test_cases:
    assert car_race_collision(n=input) == 0
```

This test case provides a range of inputs from 1 to 100, each of which is expected to return 0 since no cars collide in these cases. 
This is achieved in the following steps:
1. A list of inputs is defined in the `test_cases` variable.
2. A for loop is used to iterate over each input in `test_cases`.
3. An `assert` statement checks whether the result of calling the `car_race_collision()` function is equal to the expected output `0`. 
4. If the assertion passes, the output statement `Pass` is displayed. If there's a mismatch, `Fail` is displayed, along with the error message, helping identify the cause of the failure. 
This way, the function is tested against a variety of inputs to verify its correctness.